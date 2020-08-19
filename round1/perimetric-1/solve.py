#!/usr/bin/env python
import sys


def solver(N, W, pl, ph):
    def rooms():
        L, (al, bl, cl, dl) = pl
        H, (ah, bh, ch, dh) = ph
        l1 = l2 = 0
        h1 = h2 = 0
        for l, h in zip(L, H):
            yield (l, h)
            l2, l1 = l1, l
            h2, h1 = h1, h
        for _ in range(len(L), N):
            l = (al * l2 + bl * l1 + cl) % dl + 1
            h = (ah * h2 + bh * h1 + ch) % dh + 1
            yield (l, h)
            l2, l1 = l1, l
            h2, h1 = h1, h

    res = 1
    P = 0
    x = y = 0
    Y = [0 for _ in range(W+1)]
    for l, h in rooms():
        dx = min(W, l - x + W)
        Y = Y[dx:] + [0 for _ in range(dx)]
        Y = [Y[0]] + [max(q, h) for q in Y[1:]]
        if l > x:
            P += 2 * (W + h)
        else:
            y = Y[0]
            P += 2 * (l - x + W)
            P += 2 * max(0, h - y)
        x, y = l + W, h
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
            N, K, W = map(int, next(fp).split())
            L = list(map(int, next(fp).split()))
            a,b,c,d = map(int, next(fp).split())
            pl = (L, (a, b, c, d))
            H = list(map(int, next(fp).split()))
            a,b,c,d = map(int, next(fp).split())
            ph = (H, (a, b, c, d))
            yield (N, W, pl, ph)


if __name__ == '__main__':
    solve(*sys.argv[1:])
