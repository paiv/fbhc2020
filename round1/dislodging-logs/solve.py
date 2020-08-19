#!/usr/bin/env python
import ctypes
import sys


def solve(fn):
    lib = ctypes.cdll.LoadLibrary('libsolv.dylib')
    lib.solve.argtypes = (ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32))
    lib.solve.restype = ctypes.c_uint32

    for index, args in enumerate(parse(fn), 1):
        print(f'Case #{index}: ', end='', flush=True)
        N, M, S, (P, parg), (Q, qarg) = args
        xs = [N, M, S, *parg, *qarg, len(P), *P, *Q]
        data = (ctypes.c_uint32*len(xs))(*xs)
        r = lib.solve(len(xs), data)
        print(r, flush=True)


def parse(fn):
    with open(fn, 'rb') as fp:
        T = int(next(fp), 10)
        while T > 0:
            T -= 1
            N, M, K, S = map(int, next(fp).split())
            P = list(map(int, next(fp).split()))
            a,b,c,d = map(int, next(fp).split())
            pp = (P, (a, b, c, d))
            Q = list(map(int, next(fp).split()))
            a,b,c,d = map(int, next(fp).split())
            pq = (Q, (a, b, c, d))
            yield (N, M, S, pp, pq)


if __name__ == '__main__':
    solve(*sys.argv[1:])
