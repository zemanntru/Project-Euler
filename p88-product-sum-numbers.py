'''
We make a few observations: it isn't always true that Nb > Na where ka < kb. However, 
since N > k, we start the search at N + 1 for a given k. We define fac(n) to return
a list with entries tup = (prod_sum, num) where prod_sum is a combination of the sum of 
products of divisors of n, and num is the terms. For example, if n = 16, we have:
F(16) = [(2 + 8, 2), (4 + 4, 2), (2 + 2 + 4, 3), (2 + 2 + 2 + 2, 4)] = [(10, 2), (8, 2), (8, 3), (8, 4)].
This list is built recursively: take every divisor d that is not 1 or n, and we can append it 
to the existing tuples in the list of F(n / d), and incrementing the count by 1. However, Since F(n / d) does
not include (n / d, 1), we include (d + n / d, 2) in F(n). A dictionary is used to eliminate
repetitive tuples. Then for any given k, we look for the smallest N such that N - tup[0] = k - tup[1] holds where
the lhs represents the remainder of 1s, and the right hand side is the available remainder in the set.
Once N is found, a dictionary is used to ensure it is counted once.
'''

import math
from itertools import combinations
from functools import reduce

mems0 = [None for x in range(15000)]
mem_n, ans = {}, 0

def fac(n):
    if mems0[n] != None:
        return mems0[n]

    p, N, ls_fac, psk = 2, n, [], []
    while n > 1:
        while n % p == 0:
            ls_fac.append(p)
            n /= p
        if n == 1: break
        if p*p > n:
            ls_fac.append(int(n))
            break
        p += 1

    if len(ls_fac) == 1:
        return [(ls_fac[0], 1)]

    mems = {}
    for l in range(1, len(ls_fac)):
        for tup in set(combinations(ls_fac, l)):
            prod = reduce(lambda a,b: a*b, tup)
            if (prod + N // prod, 2) not in mems:
                mems[(prod + N // prod, 2)] = True
            for tup2 in mems0[N // prod]:
                if (tup2[0] + prod, tup2[1] + 1) not in mems:
                    mems[(tup2[0] + prod, tup2[1] + 1)] = True
    
    return list(mems.keys())

for n in range(2, 15000):
    mems0[n] = fac(n)

for k in range(2, 12001):
    N, flag = k + 1, True
    while flag == True:
        N += 1
        for x in mems0[N]:
            if N - x[0] == k - x[1]:
                flag = False
                break

    if N not in mem_n:
        mem_n[N] = True
        ans += N

print('The sum of minimal product-sum numbers for 2 <= k <= 12000: {0}'.format(ans))