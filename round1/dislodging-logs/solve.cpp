// c++ -std=c++17 -shared solve.cpp -o libsolv.dylib
#include <algorithm>
#include <cmath>
#include <cstdint>


typedef int32_t i32;
typedef uint32_t u32;
typedef uint64_t u64;


extern "C" {
    u32 solve(u32 size, const u32* data);
}


using std::abs;
using std::min;
using std::max;
using std::sort;


typedef struct {
    u32 N, M, S;
    u32 ap, bp, cp, dp;
    u32 aq, bq, cq, dq;
    u32 K;
} problem;


static constexpr u32
stream(u64 v2, u64 v1, u64 a, u64 b, u32 c, u32 d) {
    return (((v2 * a % d) + (v1 * b % d)) % d + c) % d + 1;
}


u32 solve(u32 size, const u32* data) {
    const problem& prob = *(const problem*)data;
    u32 P[prob.N];
    u32 Q[prob.M];

    {
        u32 p1=0, p2=0, q1=0, q2=0;
        const u32* pp = &data[sizeof(problem) / sizeof(u32)];
        const u32* pq = pp + prob.K;
        for (u32 i = 0; i < prob.K; ++i) {
            u32 p = *pp++;
            u32 q = *pq++;
            P[i] = p;
            Q[i] = q;
            p2 = p1;
            q2 = q1;
            p1 = p;
            q1 = q;
        }
        for (u32 i = prob.K; i < prob.N; ++i) {
            u32 p = stream(p2, p1, prob.ap, prob.bp, prob.cp, prob.dp);
            P[i] = p;
            p2 = p1;
            p1 = p;
        }
        for (u32 i = prob.K; i < prob.M; ++i) {
            u32 q = stream(q2, q1, prob.aq, prob.bq, prob.cq, prob.dq);
            Q[i] = q;
            q2 = q1;
            q1 = q;
        }

        sort(&P[0], &P[prob.N]);
        sort(&Q[0], &Q[prob.M]);
    }

    auto F = [P=&P[0], pend=&P[prob.N], Q=&Q[0], qend=&Q[prob.M]](u32 t) -> u32 {
        auto* q = Q;
        for (auto* p = P; p != pend && q != qend; ++p) {
            auto q0 = *q;
            while (q != qend && (min(abs(i32(q0 - *p)), abs(i32(*q - *p))) + (*q - q0) <= t)) {
                ++q;
            }
        }
        return q == qend;
    };

    u32 res = 0;
    for (u32 l=0, r=500000001; l < r;) {
        u32 t = (l + r) / 2;
        if (F(t) == 0) {
            l = t + 1;
        }
        else {
            res = t;
            r = t;
        }
    }

    return res;
}
