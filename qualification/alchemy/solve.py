#!/usr/bin/env python
import sys


def solve(fn):
    for index, shards in enumerate(parse(fn), 1):
        print(f'Case #{index}: ', end='', flush=True)
        a = shards.count(ord('A'))
        b = shards.count(ord('B'))
        print('Y' if (abs(a-b) == 1) else 'N')


def parse(fn):
    state = 0
    with open(fn, 'rb') as fp:
        T = int(next(fp))
        for _ in range(T):
            N = int(next(fp))
            s = next(fp).strip()
            yield s


if __name__ == '__main__':
    solve(*sys.argv[1:])
