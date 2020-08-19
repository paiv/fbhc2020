#!/usr/bin/env python
import sys
from collections import defaultdict


def cut_trees(section):
    section = sorted(section)
    R = defaultdict(int)
    L = defaultdict(int)
    res = 0

    for p, h in section:
        R[p + h] = max(R[p + h], R[p] + h)

    for p, h in reversed(section):
        L[p - h] = max(L[p - h], L[p] + h)

    res = max(R.values())
    for p, h in L.items():
        res = max(res, R[p] + h)

    return res


def solve(fn):
    for index, args in enumerate(parse(fn), 1):
        print(f'Case #{index}: ', end='', flush=True)
        res = cut_trees(*args)
        print(res, flush=True)


def parse(fn):
    with open(fn, 'rb') as fp:
        T = int(next(fp))
        for _ in range(T):
            N = int(next(fp))
            section = [tuple(map(int, next(fp).split())) for _ in range(N)]
            yield (section, )


if __name__ == '__main__':
    solve(*sys.argv[1:])
