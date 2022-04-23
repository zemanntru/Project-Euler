'''
Solved via direct computation. For each number, find the sum of proper divisors. 
Use this to check whether the number is abundant. Append this to a list. Then,
mark off a boolean array with all numbers that are the sum of two abundant numbers.
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

mxn = 28124
bsum = [False for i in range(mxn)]
abun = []

for n in range(2, mxn):
    if sdiv(n) > n:
        abun.append(n)

# This takes a few seconds to run but not excessive
for i in range(len(abun)):
    for j in range(len(abun)):
        if abun[i] + abun[j] < mxn:
            bsum[abun[i] + abun[j]] = True

ans = 0
for n in range(1, mxn):
    if not bsum[n]:
        ans += n

print('Sum of all positive integers that are not a sum of two abundant numbers: {0}'.format(ans))

