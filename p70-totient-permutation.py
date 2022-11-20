'''
We calculate the totient function through prime factorization for 1 < n < 10^7. To speed
up this process, we memoise values seen before, where the initial case if for all primes p
totient(p) = p - 1. To check for permutations, we do a frequency count of each digit.
'''

from collections import Counter
import math

mxn = 10000000
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
    
    return memo[xf]


ans, mn = 0, mxn
for n in range (2, mxn):
    nfac = factor(n)
    if Counter(str(int(n))) == Counter(str(int(nfac))):
        if n / nfac < mn:
            mn, ans = n / nfac, n

print('The n that has the same permutation as totient(n) and ratio minimized: {0}'.format(ans))
