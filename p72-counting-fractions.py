'''
The set of irreducible fractions with denominator d is the number of n relatively prime to d,
in other words, totient(d). Hence, this problem is adding up totient(d) for 2 <= d <= 1000000
'''

import math

mxn = int(1e6) + 1
memo, prime, p = [False for n in range(mxn)], [True for i in range(mxn)], 2
lpr = []
while (p*p <= mxn):
    if prime[p]:
        for i in range(p*p, mxn, p):
            prime[i] = False
    p += 1

for p in range(2, mxn):
    if prime[p] == True:
        memo[p] = p - 1
        lpr.append(p)

def factor(x):
    if memo[int(x)] != False:
        return memo[int(x)]
    p, xf = 2, int(x)
    memo[xf] = 1
    for p in lpr:
        if x % p == 0:
            cnte = 0
            while x % p == 0:
                cnte += 1
                x /= p
            memo[xf] *= memo[p] * math.pow(p, cnte - 1)
            if memo[int(x)] != False:
                memo[xf] *= memo[int(x)]
                break
        if x == 1: 
            break
        if p*p > x:
            memo[xf] *= memo[int(x)]
            break
    return int(memo[xf])

print('The number of elements in the reduced set of proper functions are: {0}'.format(sum([factor(x) for x in range(2, mxn)])))