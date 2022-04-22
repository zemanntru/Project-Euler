'''
The answer here is 40C20, however, this number is probably too big to be computed directly.
Note, this simplfies to 40*39*...*21/20*19*...*1. We do a prime factorization of both
numerator and denominator, and use that to simplify the quotient. 
'''
import math
num = {}
denom = {}

def count_divisors(n, bnum):
    p = 2
    while n > 1:
        if n % p == 0:
            cnt = 0
            while n % p == 0:
                n /= p
                cnt += 1
            if bnum == True:
                if p not in num:
                    num[p] = cnt
                else:
                    num[p] += cnt 
            else:
                if p not in denom:
                    denom[p] = cnt
                else:
                    denom[p] += cnt
        if n == 1: break
        if p*p > n:
            if bnum == True:
                if n not in num:
                    num[n] = 1
                else:
                    num[n] += 1 
            else:
                if n not in denom:
                    denom[n] = 1
                else:
                    denom[n] += 1
            break
        p += 1

for x in range(21, 41):
    count_divisors(x, True)

for x in range(2, 21):
    count_divisors(x, False)

ans = 1
for p, n in num.items():
    if p in denom:
        ans *= int(math.pow(p, n - denom[p]))
    else:
        ans *= int(math.pow(p, n))

print('number of paths in a 20x20 grid: {0}'.format(ans))

