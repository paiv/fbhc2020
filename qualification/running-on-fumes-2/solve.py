#!/usr/bin/env python
import sys
from collections import deque


def travel(tank_capacity, A, B, costs):
    res = 0
    return res


def solve(fn):
    for index, args in enumerate(parse(fn), 1):
        print(f'Case #{index}: ', end='', flush=True)
        res = travel(*args)
        print(res, flush=True)


def parse(fn):
    state = 0
    costs = None
    with open(fn, 'rb') as fp:
        T = int(next(fp))
        for _ in range(T):
            N, M, A, B = map(int, next(fp).split())
            costs = [tuple(map(int, next(fp).split())) for _ in range(N)]
            yield (M, A, B, costs)


if __name__ == '__main__':
    solve(*sys.argv[1:])
