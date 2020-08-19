#!/usr/bin/env python
import sys


def solver(rule_in, rule_out):
    n = len(rule_in)

    direct = dict()
    for i in range(n):
        direct[(i, i)] = 1
    for i in range(n-1):
        direct[(i, i+1)] = (rule_out[i] and rule_in[i+1])
        direct[(i+1, i)] = (rule_out[i+1] and rule_in[i])

    def fly(src, dest):
        if src <= dest:
            return all(direct[(i, i+1)] for i in range(src, dest))
        return all(direct[(i, i-1)] for i in range(dest+1, src+1))

    def can_fly(src):
        for dest in range(n):
            yield 'Y' if fly(src, dest) else 'N'

    res = (''.join(can_fly(i)) for i in range(n))
    return '\n'.join(res)


def solve(fn):
    for index, args in enumerate(parse(fn), 1):
        print(f'Case #{index}: ', flush=True)
        res = solver(*args)
        print(res, flush=True)


def parse(fn):
    rule_in = rule_out = None
    state = 0
    with open(fn) as fp:
        T = int(next(fp))
        for _ in range(T):
            N = int(next(fp))
            rule_in = [(x == 'Y') for x in next(fp).strip()]
            rule_out = [(x == 'Y') for x in next(fp).strip()]
            yield (rule_in, rule_out)


if __name__ == '__main__':
    solve(*sys.argv[1:])
