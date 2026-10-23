import torch
from torch import nn
from torch.nn import functional as F

EPS = 1e-6
DENSITY_SCALES = (5, 17, 49)
MORPH_DIM = len(DENSITY_SCALES) + 7
OBSERVED = len(DENSITY_SCALES)


def smooth(values, kernel):
    kernel = min(int(kernel), values.size(-1))
    if kernel % 2 == 0:
        kernel -= 1
    if kernel < 3:
        return values
    return F.avg_pool1d(values, kernel, stride=1, padding=kernel // 2, count_include_pad=False)


def normalise(x, mask):
    observed = torch.isfinite(x) & (mask > 0)
    zero = torch.zeros((), dtype=x.dtype, device=x.device)
    clean = torch.where(observed, x, zero)
    m = observed.to(x.dtype)
    count = m.sum(1, keepdim=True)
    safe = count.clamp_min(1.0)
    mean = (clean.sum(1, keepdim=True) / safe).detach()
    centred = torch.where(observed, clean - mean, zero)
    scale = (centred.square().sum(1, keepdim=True) / safe + EPS).sqrt()
    scale = torch.where(count > 1, scale, torch.ones_like(scale)).detach()
    return centred / scale, m, mean, scale


def gap_geometry(observed):
    b, n, t = observed.shape
    pos = torch.arange(t, device=observed.device).view(1, 1, t).expand(b, n, t)
    horizon = torch.full_like(pos, t)
    left_index = torch.where(observed, pos, torch.full_like(pos, -1)).cummax(-1).values
    right_index = torch.where(observed, pos, horizon).flip(-1).cummin(-1).values.flip(-1)
    left = torch.where(left_index >= 0, pos - left_index, horizon)
    right = torch.where(right_index < t, right_index - pos, horizon)
    bounded = (left_index >= 0) & (right_index < t)
    gap = torch.where(observed, torch.zeros_like(pos),
                      torch.where(bounded, right_index - left_index - 1, horizon))
    return (left.to(torch.float32), right.to(torch.float32), gap.to(torch.float32),
            left_index, right_index)


def interpolate_gaps(values, observed, left_index, right_index):
    t = values.size(-1)
    pos = torch.arange(t, device=values.device).view(1, 1, t).expand_as(values)
    left_value = values.gather(-1, left_index.clamp_min(0))
    right_value = values.gather(-1, right_index.clamp_max(t - 1))
    has_left, has_right = left_index >= 0, right_index < t
    span = (right_index - left_index).clamp_min(1).to(values.dtype)
    weight = (pos - left_index).to(values.dtype) / span
    between = left_value * (1 - weight) + right_value * weight
    filled = torch.where(has_left & has_right, between,
                         torch.where(has_left, left_value,
                                     torch.where(has_right, right_value, torch.zeros_like(values))))
    return torch.where(observed, values, filled)


def clip_geometry(left, right, gap, limit, t):
    two_sided = (left < t) & (right < t)
    left = torch.where(two_sided, left.clamp(max=limit), left)
    right = torch.where(two_sided, right.clamp(max=limit), right)
    gap = torch.where(two_sided, gap.clamp(max=2.0 * limit + 1.0), gap)
    return left, right, gap


def morphology(m, clip=0.0):
    mv = m.transpose(1, 2)
    b, n, t = mv.shape
    flat = mv.reshape(b * n, 1, t)
    densities = [smooth(flat, k).reshape(b, n, t) for k in DENSITY_SCALES]
    left, right, gap, _, _ = gap_geometry(mv > 0)
    if clip:
        left, right, gap = clip_geometry(left, right, gap, float(clip), t)
    nearest = torch.minimum(left, right)
    if clip:
        nearest = nearest.clamp(max=float(clip))
    rate = mv.mean(-1, keepdim=True).expand(b, n, t)
    window = mv.mean((1, 2)).view(b, 1, 1).expand(b, n, t)
    horizon = float(t)
    return torch.stack(densities + [mv, gap / horizon, left / horizon, right / horizon,
                                    nearest / horizon, rate, window], -1)


def starting_point(x, mask, clip=0.0):
    normalised, m, mean, scale = normalise(x, mask)
    observed = (m > 0).transpose(1, 2)
    series = normalised.transpose(1, 2)
    left, right, _, left_index, right_index = gap_geometry(observed)
    estimate = interpolate_gaps(series, observed, left_index, right_index)
    depth = torch.minimum(left, right)
    if clip:
        depth = depth.clamp(max=float(clip))
    support = torch.where(observed, torch.ones_like(depth), 1.0 / (1.0 + depth))
    return dict(series=series, observed=observed, estimate=estimate, support=support,
                morph=morphology(m, clip), mean=mean, scale=scale)


def pad_to_blocks(values, block):
    t = values.size(2)
    block = max(1, min(int(block), t))
    count = (t + block - 1) // block
    pad = count * block - t
    if pad:
        values = torch.cat([values, values[:, :, -1:].expand(-1, -1, pad, -1)], 2)
    return values, count, block


def upsample_time(values, length):
    b, n, c, _ = values.shape
    flat = values.reshape(b * n, c, 1).transpose(1, 2)
    if c != length:
        flat = F.interpolate(flat, size=length, mode='linear', align_corners=False)
    return flat.reshape(b, n, length)


class DropPath(nn.Module):
    def __init__(self, probability):
        super().__init__()
        self.probability = float(probability)

    def forward(self, x):
        if not self.training or self.probability <= 0:
            return x
        keep = 1.0 - self.probability
        shape = (x.size(0),) + (1,) * (x.dim() - 1)
        return x * torch.bernoulli(torch.full(shape, keep, device=x.device, dtype=x.dtype)) / keep


class Residual(nn.Module):
    def __init__(self, width, drop_path, init=1e-2):
        super().__init__()
        self.gamma = nn.Parameter(torch.full((width,), float(init)))
        self.drop = DropPath(drop_path)

    def forward(self, x, branch):
        return x + self.drop(self.gamma * branch)


class Stem(nn.Module):
    def __init__(self, width, kernel=5):
        super().__init__()
        self.proj = nn.Conv1d(2 + MORPH_DIM, width, kernel, padding=kernel // 2)
        self.norm = nn.LayerNorm(width)

    def forward(self, estimate, support, morph):
        b, n, t = estimate.shape
        x = torch.cat([estimate.unsqueeze(-1), support.unsqueeze(-1), morph], -1)
        x = x.reshape(b * n, t, -1).transpose(1, 2)
        return self.norm(self.proj(x)[..., :t].transpose(1, 2).reshape(b, n, t, -1))


class TemporalBlock(nn.Module):
    def __init__(self, width, kernel=5, dilations=(1, 4, 16), dense_kernel=31, ffn_ratio=2.0,
                 drop_path=0.0, dropout=0.0, gain_cap=4.0):
        super().__init__()
        self.gain_cap = float(gain_cap)
        self.norm1 = nn.LayerNorm(width)
        branches = [nn.Conv1d(width, width, kernel, padding=d * (kernel - 1) // 2,
                              dilation=d, groups=width) for d in dilations]
        branches.append(nn.Conv1d(width, width, dense_kernel, padding=dense_kernel // 2, groups=width))
        self.branches = nn.ModuleList(branches)
        self.mix = nn.Linear(width, width)
        self.res1 = Residual(width, drop_path)
        self.norm2 = nn.LayerNorm(width)
        hidden = max(int(width * ffn_ratio), width)
        self.ffn = nn.Sequential(nn.Linear(width, hidden), nn.GELU(),
                                 nn.Dropout(dropout), nn.Linear(hidden, width))
        self.res2 = Residual(width, drop_path)

    def support_gain(self, observed, branch, steps):
        kernel = branch.kernel_size[0]
        ones = observed.new_ones(1, 1, kernel)
        count = F.conv1d(observed, ones, padding=branch.padding[0],
                         dilation=branch.dilation[0])[..., :steps]
        gain = (kernel / count.clamp_min(1.0)).clamp(max=self.gain_cap)
        return torch.where(count > 0, gain, torch.zeros_like(gain))

    def forward(self, h, morph):
        b, n, t, w = h.shape
        observed = morph[..., OBSERVED].reshape(b * n, 1, t)
        flat = self.norm1(h).reshape(b * n, t, w).transpose(1, 2) * observed
        pooled = None
        for branch in self.branches:
            piece = branch(flat)[..., :t] * self.support_gain(observed, branch, t)
            piece = piece.transpose(1, 2).reshape(b, n, t, w) / len(self.branches)
            pooled = piece if pooled is None else pooled + piece
        h = self.res1(h, self.mix(pooled))
        return self.res2(h, self.ffn(self.norm2(h)))


class CrossVariableAttention(nn.Module):
    def __init__(self, width, heads, dropout=0.0, drop_path=0.0):
        super().__init__()
        self.heads, self.head_width = int(heads), width // int(heads)
        self.norm = nn.LayerNorm(width)
        self.query = nn.Linear(width, width)
        self.key = nn.Linear(width, width)
        self.value = nn.Linear(width, width)
        self.out = nn.Linear(width, width)
        self.drop = nn.Dropout(dropout)
        self.res = Residual(width, drop_path)

    def forward(self, h, morph):
        b, n, t, w = h.shape
        heads, hw = self.heads, self.head_width
        y = self.norm(h)
        weight = morph[..., OBSERVED].unsqueeze(-1)
        pooled = (y * weight).sum(2) / weight.sum(2).clamp_min(1.0)
        q = self.query(pooled).reshape(b, n, heads, hw).transpose(1, 2)
        k = self.key(pooled).reshape(b, n, heads, hw).transpose(1, 2)
        weights = self.drop((q @ k.transpose(-1, -2) * hw ** -0.5).softmax(-1))
        v = self.value(y).reshape(b, n, t, heads, hw).permute(0, 3, 1, 2, 4)
        message = (weights @ v.reshape(b, heads, n, t * hw)).reshape(b, heads, n, t, hw)
        return self.res(h, self.out(message.permute(0, 2, 3, 1, 4).reshape(b, n, t, w)))


class MeasurementAnchoredAttention(nn.Module):
    def __init__(self, width, heads, dropout=0.0, drop_path=0.0):
        super().__init__()
        self.heads, self.head_width = int(heads), width // int(heads)
        self.register_buffer('slopes', torch.tensor([2.0 ** -i for i in range(self.heads)]),
                             persistent=False)
        self.norm = nn.LayerNorm(width)
        self.query = nn.Linear(width, width)
        self.key = nn.Linear(width, width)
        self.value = nn.Linear(width, width)
        self.out = nn.Linear(width, width)
        nn.init.zeros_(self.out.weight)
        nn.init.zeros_(self.out.bias)
        self.drop = nn.Dropout(dropout)
        self.res = Residual(width, drop_path)

    def forward(self, h, morph):
        b, n, t, w = h.shape
        heads, hw = self.heads, self.head_width
        y = self.norm(h).reshape(b * n, t, w)

        def split(z):
            return z.reshape(b * n, t, heads, hw).transpose(1, 2)

        q, k, v = split(self.query(y)), split(self.key(y)), split(self.value(y))
        observed = morph[..., OBSERVED].reshape(b * n, 1, 1, t) > 0.5
        pos = torch.arange(t, device=h.device, dtype=h.dtype)
        distance = (pos.view(1, t) - pos.view(t, 1)).abs()
        logits = (q @ k.transpose(-1, -2)) * hw ** -0.5
        logits = logits - self.slopes.view(1, heads, 1, 1) * distance
        weights = self.drop(logits.masked_fill(~observed, -1e9).softmax(-1))
        mass = observed.any(-1, keepdim=True).to(h.dtype)
        mean = (weights / mass.clamp_min(1e-6)) @ v
        answer = (mass * mean).transpose(1, 2).reshape(b, n, t, w)
        return self.res(h, self.out(answer))


class ReconstructionHead(nn.Module):
    def __init__(self, width, patch=8, bins=4):
        super().__init__()
        self.patch, self.bins = int(patch), int(bins)
        hidden = max(width // 2, 8)
        self.norm = nn.LayerNorm(width)

        def branch():
            return nn.Sequential(nn.Linear(width, hidden), nn.GELU(), nn.Linear(hidden, 1))

        self.local, self.segment, self.window = branch(), branch(), branch()
        self.select = nn.Linear(MORPH_DIM, 3)
        nn.init.zeros_(self.select.weight)
        nn.init.zeros_(self.select.bias)
        self.confidence = nn.Sequential(nn.Linear(width + MORPH_DIM, hidden), nn.GELU(),
                                        nn.Linear(hidden, 1))

    def forward(self, h, morph):
        b, n, t, w = h.shape
        h = self.norm(h)
        local = self.local(h).squeeze(-1)
        bins = min(self.bins, t)
        padded, count, block = pad_to_blocks(h, self.patch)
        patches = padded.reshape(b, n, count, block, w).mean(3)
        pooled = F.adaptive_avg_pool1d(h.reshape(b * n, t, w).transpose(1, 2), bins)
        segment = upsample_time(self.segment(patches), t)
        window = upsample_time(self.window(pooled.transpose(1, 2).reshape(b, n, bins, w)), t)
        candidates = torch.stack((local, segment, window), -1)
        estimate = (candidates * (self.select(morph) + 1.0 / 3.0)).sum(-1)
        confidence = torch.sigmoid(self.confidence(torch.cat((h, morph), -1)).squeeze(-1))
        return estimate, confidence


class Stage(nn.Module):
    def __init__(self, width, depth, heads, kernel, dilations, dense_kernel, ffn_ratio,
                 dropout, drop_path, attn_dropout, cross_every, patch, bins):
        super().__init__()
        self.stem = Stem(width, kernel)
        self.blocks = nn.ModuleList()
        self.routers = nn.ModuleDict()
        for i in range(depth):
            self.blocks.append(TemporalBlock(width, kernel, dilations, dense_kernel, ffn_ratio,
                                             drop_path, dropout))
            if (i + 1) % cross_every == 0:
                self.routers[str(i)] = CrossVariableAttention(width, heads, attn_dropout, drop_path)
        self.anchor = MeasurementAnchoredAttention(width, heads, attn_dropout, drop_path)
        self.head = ReconstructionHead(width, patch, bins)

    def forward(self, estimate, support, morph):
        h = self.stem(estimate, support, morph)
        for i, block in enumerate(self.blocks):
            h = block(h, morph)
            if str(i) in self.routers:
                h = self.routers[str(i)](h, morph)
        h = self.anchor(h, morph)
        return self.head(h, morph)


class Fusion(nn.Module):
    BINS, RANGE = 640, 10.0

    def __init__(self, features, length, screen_limit=3.0, window_prior=8.0):
        super().__init__()
        c, t = int(features), int(length)
        for name, shape in (('count', (c,)), ('total', (c,)), ('pairs', (c, c)),
                            ('pair_sum', (c, c)), ('pair_product', (c, c)),
                            ('lag_pairs', (t, c)), ('lag_sum', (t, c)),
                            ('histogram', (c, self.BINS + 2))):
            self.register_buffer(name, torch.zeros(shape, dtype=torch.float64))
        self.screen_limit = float(screen_limit)
        self.window_prior = float(window_prior)
        self.log_scale = nn.Parameter(torch.zeros(c))

    @torch.no_grad()
    def accumulate(self, x, m):
        x, m = x.double(), m.double()
        self.count += m.sum((0, 1))
        self.total += (m * x).sum((0, 1))
        flat_m, flat_x = m.reshape(-1, m.shape[-1]), (m * x).reshape(-1, m.shape[-1])
        self.pairs += flat_m.T @ flat_m
        self.pair_sum += flat_x.T @ flat_m
        self.pair_product += flat_x.T @ flat_x
        for h in range(1, x.shape[1]):
            both = m[:, h:] * m[:, :-h]
            self.lag_pairs[h] += both.sum((0, 1))
            self.lag_sum[h] += (both * 0.5 * (x[:, h:] - x[:, :-h]).square()).sum((0, 1))
        width = 2 * self.RANGE / self.BINS
        slot = (torch.floor((x + self.RANGE) / width).clamp(-1, self.BINS) + 1).long()
        index = (slot + torch.arange(x.shape[-1], device=x.device) * (self.BINS + 2)).reshape(-1)
        self.histogram.view(-1).index_add_(0, index, m.reshape(-1))

    def ready(self):
        return bool(self.count.min() > 1000 and (self.lag_pairs[1:] > 0).any(0).all())

    def screen(self):
        width = 2 * self.RANGE / self.BINS
        centres = -self.RANGE + width * (torch.arange(self.BINS + 2, device=self.histogram.device,
                                                      dtype=torch.float64) - 0.5)
        weight = self.histogram / self.histogram.sum(1, keepdim=True).clamp_min(1.0)

        def weighted_median(values, w):
            order = torch.argsort(values, dim=-1)
            cdf = torch.cumsum(torch.gather(w, -1, order), -1)
            pick = torch.searchsorted(cdf, torch.full_like(cdf[:, :1], 0.5)).clamp(max=values.shape[-1] - 1)
            return torch.gather(torch.gather(values, -1, order), -1, pick)

        median = weighted_median(centres.expand_as(weight), weight)
        mad = weighted_median((centres - median).abs(), weight).squeeze(-1)
        mean = self.total / self.count
        std = (self.pair_product.diagonal() / self.count - mean.square()).clamp_min(0).sqrt()
        return std / (1.4826 * mad.clamp_min(0.5 * width)) <= self.screen_limit

    def statistics(self):
        mean = self.total / self.count
        pairs = self.pairs.clamp_min(1.0)
        left, right = self.pair_sum / pairs, self.pair_sum.T / pairs
        cov = self.pair_product / pairs - left * right
        cov = 0.5 * (cov + cov.T)
        values, vectors = torch.linalg.eigh(cov)
        values = values.clamp_min(1e-3 * cov.diagonal().mean())
        cov = (vectors * values) @ vectors.T
        gamma = self.lag_sum / self.lag_pairs.clamp_min(1.0)
        gamma[0] = 0.0
        gaps = self.lag_pairs[1:] == 0
        for v in gaps.any(0).nonzero().flatten().tolist():
            lags = torch.arange(gamma.shape[0], device=gamma.device, dtype=gamma.dtype)
            known = torch.cat((gaps.new_ones(1), ~gaps[:, v]))
            xs, ys = lags[known], gamma[known, v]
            right = torch.searchsorted(xs, lags).clamp(1, xs.numel() - 1)
            x0, x1, y0, y1 = xs[right - 1], xs[right], ys[right - 1], ys[right]
            filled = torch.where(lags > xs[-1], ys[-1], y0 + (y1 - y0) * (lags - x0) / (x1 - x0))
            gamma[:, v] = torch.where(known, gamma[:, v], filled)
        return mean, cov, torch.cummax(gamma, 0).values

    @staticmethod
    def mce(y, o, mean, cov):
        centred = o * (y - mean)
        eye = torch.eye(o.shape[-1], dtype=o.dtype, device=o.device)
        system = cov * o.unsqueeze(1) * o.unsqueeze(2) + eye * (1 - o).unsqueeze(1) + 1e-6 * eye
        inverse = torch.linalg.inv(system)
        solved = (inverse @ centred.unsqueeze(-1)).squeeze(-1)
        cross = mean + solved @ cov
        lever = (cov * o.unsqueeze(1)) @ inverse
        v_cond = (cov.diagonal() - (lever * (cov * o.unsqueeze(1))).sum(-1)).clamp_min(1e-6)
        pivot = inverse.diagonal(dim1=1, dim2=2)
        loo = mean + centred - solved / pivot
        return cross, v_cond, loo, 1.0 / pivot

    def forward(self, answer, x, m):
        b, t, c = answer.shape
        mean, cov, gamma = self.statistics()
        steps = torch.arange(t, device=x.device).view(1, t, 1).expand(b, t, c)
        far = torch.full_like(steps, -10 * t)
        last = torch.cummax(torch.where(m, steps, far), 1).values
        following = -torch.flip(torch.cummax(torch.flip(torch.where(m, -steps, far), [1]), 1).values, [1])
        distance = torch.minimum(steps - last, following - steps).clamp(0, t - 1)
        g = torch.gather(gamma.T.to(answer.dtype).unsqueeze(0).expand(b, c, t), 2,
                         distance.transpose(1, 2)).transpose(1, 2)
        v_time = (self.log_scale.exp() * g).clamp_min(1e-8)

        keep = self.screen()
        o = (m & keep).reshape(-1, c).double()
        y = torch.where(m, x, torch.zeros_like(x)).reshape(-1, c).double()
        cross, v_cond, loo, loo_var = self.mce(y, o, mean, cov)

        residual = (o * (y - loo).square()).reshape(b, t, c).sum(1, keepdim=True)
        spread = (o * loo_var).reshape(b, t, c).sum(1, keepdim=True)
        seen = o.reshape(b, t, c).sum(1, keepdim=True)
        unit = spread / seen.clamp_min(1.0)
        alpha = torch.where(seen > 0, (residual + self.window_prior * unit)
                            / (spread + self.window_prior * unit).clamp_min(1e-12),
                            torch.ones_like(seen)).clamp_min(1e-3)
        v_prior = (alpha * cov.diagonal()).expand(b, t, c)
        v_cross = (alpha * v_cond.reshape(b, t, c)).clamp(min=1e-3 * v_prior)
        v_cross = torch.minimum(v_cross, v_prior)

        information = 1.0 / v_cross - 1.0 / v_prior
        cross, mu = cross.reshape(b, t, c), mean.view(1, 1, c)
        shift = (information * mu + (cross - mu) / v_cross).to(answer.dtype)
        information = information.to(answer.dtype)
        shift = torch.where(keep, shift, torch.zeros_like(shift))
        information = torch.where(keep, information, torch.zeros_like(information))
        fused = answer + (shift - information * answer) / (1.0 / v_time + information)
        return torch.where(m, x, fused)


class Cairn(nn.Module):
    def __init__(self, features, length, width=96, depth=4, stages=2, kernel=5,
                 dilations=(1, 4, 16), dense_kernel=31, ffn_ratio=2.0, dropout=0.2,
                 drop_path=0.2, attn_dropout=0.2, heads=8, cross_every=2, patch=8, bins=4,
                 screen_limit=3.0, window_prior=8.0, clip=12.0):
        super().__init__()
        if width % heads:
            raise ValueError('width must be divisible by heads')
        self.clip = float(clip)
        self.stages = nn.ModuleList([
            Stage(width, depth, heads, kernel, dilations, dense_kernel, ffn_ratio, dropout,
                  drop_path, attn_dropout, cross_every, patch, bins) for _ in range(stages)])
        self.fusion = Fusion(features, length, screen_limit, window_prior)

    def temporal(self, x, mask):
        state = starting_point(x, mask, 0.0 if self.training else self.clip)
        observed, series, morph = state['observed'], state['series'], state['morph']
        estimate, support = state['estimate'], state['support']
        for stage in self.stages:
            correction, confidence = stage(estimate, support, morph)
            estimate = torch.where(observed, series, estimate + correction)
            support = torch.where(observed, torch.ones_like(confidence), confidence)
        return estimate.transpose(1, 2) * state['scale'] + state['mean'], observed

    def forward(self, x, mask):
        answer, observed = self.temporal(x, mask)
        measured = observed.transpose(1, 2)
        clean = torch.where(measured, x, torch.zeros_like(x))
        if self.training:
            self.fusion.accumulate(clean, measured)
        if not self.fusion.ready():
            return answer
        return self.fusion(answer, clean, measured)
