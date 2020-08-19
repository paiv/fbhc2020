#!/usr/bin/env python
import sys
from collections import deque


def travel(tank_capacity, costs):
    L = deque([(0, 0)])
    for i, x in enumerate(costs[1:], 1):
        while L:
            j, w = L[0]
            if (i - j <= tank_capacity): break
            L.popleft()

        if not L: return -1

        if x:
            _, G = L[0]
            F = (G + x)
            while L:
                _, w = L[-1]
                if w < F: break
                L.pop()

            L.append((i, F))

    _, res = L[0]
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
            N, M = map(int, next(fp).split())
            costs = list(map(int, (next(fp) for _ in range(N))))
            yield (M, costs)


if __name__ == '__main__':
    solve(*sys.argv[1:])
