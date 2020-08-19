#!/usr/bin/env python
import sys
from bisect import bisect_left


def solver(N, pl, pw, ph):
    def rooms():
        L, (al, bl, cl, dl) = pl
        W, (aw, bw, cw, dw) = pw
        H, (ah, bh, ch, dh) = ph
        l1 = l2 = 0
        w1 = w2 = 0
        h1 = h2 = 0
        for l, w, h in zip(L, W, H):
            yield (l, w, h)
            l2, l1 = l1, l
            w2, w1 = w1, w
            h2, h1 = h1, h
        for _ in range(len(L), N):
            l = (al * l2 + bl * l1 + cl) % dl + 1
            w = (aw * w2 + bw * w1 + cw) % dw + 1
            h = (ah * h2 + bh * h1 + ch) % dh + 1
            yield (l, w, h)
            l2, l1 = l1, l
            w2, w1 = w1, w
            h2, h1 = h1, h

    def intersects_le(a, b):
        la, wa, ha = a
        lb, wb, hb = b
        return (lb <= la + wa)

    def intersects_ge(a, b):
        la, wa, ha = a
        lb, wb, hb = b
        return (la <= lb + wb)

    def collapse(intervals, k):
        (l, w, h) = k
        if not intervals:
            return (k, 2 * (w + h))
        dp = 0
        dp += 2 * max(0, intervals[0][0] - l)
        r = l + w
        dp += 2 * max(0, r - (intervals[-1][0] + intervals[-1][1]))
        for p, q in zip(intervals, intervals[1:]):
            (lx, wx, hx) = p
            (lu, wu, hu) = q
            dp += 2 * (lu - (lx + wx))
            dp -= 2 * h
        for (lx, wx, hx) in intervals:
            l = min(l, lx)
            r = max(r, lx + wx)
            h = max(h, hx)
        return (l, r - l, h), dp

    P = 0
    res = 1
    unions = list()

    for l, w, h in rooms():
        k = (l, w, h)
        i = bisect_left(unions, k)
        if (i < len(unions)) or len(unions):
            j = i
            while (i > 0) and intersects_le(unions[i-1], k):
                i -= 1
            while (j < len(unions)) and intersects_ge(unions[j], k):
                j += 1
            k, dp = collapse(unions[i:j], k)
            unions[i:j] = [k]
        else:
            unions.insert(i, k)
            dp = 2 * (w + h)

        P += dp
        res = (res * P) % 1_000_000_007
    return res


def solve(fn):
    for index, args in enumerate(parse(fn), 1):
        print(f'Case #{index}: ', end='', flush=True)
        r = solver(*args)
        print(r, flush=True)


def parse(fn):
    with open(fn, 'rb') as fp:
        T = int(next(fp), 10)
        while T > 0:
            T -= 1
            N, K = map(int, next(fp).split())
            L = list(map(int, next(fp).split()))
            a,b,c,d = map(int, next(fp).split())
            pl = (L, (a, b, c, d))
            W = list(map(int, next(fp).split()))
            a,b,c,d = map(int, next(fp).split())
            pw = (W, (a, b, c, d))
            H = list(map(int, next(fp).split()))
            a,b,c,d = map(int, next(fp).split())
            ph = (H, (a, b, c, d))
            yield (N, pl, pw, ph)


if __name__ == '__main__':
    solve(*sys.argv[1:])
