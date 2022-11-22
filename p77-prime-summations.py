'''
We use Euler's recurrence for finding partitions. The number of prime partitions 
is given by: F(N) = 1/N * (sumfac(N) + sum(sumfac(x) * F(N - x) for 2 <= x < N - 1)),
where sumfac is the sum of all prime divisors. The base case is F(1) = 0, and a cache
is used wherever possible to speed up the process. 
'''

import math

dp, sfac, N = [0]*2, [0]*2, 2

def sumfac(x):
    if x < len(sfac):
        return sfac[x]

    sfac.append(0)
    if x == len(sfac):
        print(x, len(sfac))
        assert False

    n, p, ret = x, 2, 0
    while n > 1:
        if n % p == 0:
            sfac[x] += p
            while n % p == 0:
                n /= p

        if n == 1: break
        if p*p > n:
            sfac[x] += n
            break
        p += 1

    return sfac[x]

while dp[N - 1] <= 5000:
    dp.append((sumfac(N) + sum(sumfac(x) * dp[N - x] for x in range(2, N - 1))) / N)
    N += 1

print('The first value that can be written as the sum of primes in over 5000 ways: {0}'.format(N - 1))