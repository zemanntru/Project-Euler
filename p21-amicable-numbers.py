'''
Solved via direct computation. For each number, find the sum of proper divisors, 
and use this to check for the amicable pair.
'''
import math, itertools

def sdiv(n):
    fac = []
    p = 2
    ret = 0
    while n > 1:
        while n % p == 0:
            n /= p
            fac.append(p)
        if n == 1: break
        if p*p > n:
            fac.append(n)
            break
        p += 1
    '''
    using the list of prime factors, we generate distinct appearances 
    to emulate the full range of proper divisors. Note the original
    number is not included
    '''
    for n in range(1, len(fac)):
        perm = list(map(list, set(itertools.combinations(fac, n))))
        for tup in perm:
            prod = 1
            for x in tup:
                prod *= x
            ret += prod

    return int(ret + 1)

ans = 0
for x in range(1, 10000):
    p0 = sdiv(x)
    if x != p0 and x == sdiv(p0):
        ans += x

print('Sum of amicable numbers below 10000: {0}'.format(ans))

