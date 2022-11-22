'''
We use Euler's recurrence for generating partitions. Let p(n) be the
number of partitions for n, then the recursive process
is p(n) = sum((-1)^(k + 1) * p(n - k(3k - 1)/2) for k in Z, k != 0). The lower
bound for a non-zero p(n - k(3k - 1)/2) is -(sqrt(24*N + 1) - 1) / 6 and the
upper bound would be (sqrt(24*N + 1) + 1) / 6. Since the answer wants modulo 
1 million, it is congruent to taking the modulo at each stage of adding
recurrent terms.
'''

import math
mxn = mod = int(1e6)
dp, N = [1, 1] + [0] * mxn, 2

while dp[N - 1] != 0:
    lo = -int(math.ceil((math.sqrt(24*N + 1) - 1) / 6))
    hi = int(math.floor((math.sqrt(24*N + 1) + 1) / 6)) + 1
    for x in range(lo, hi):
        if x != 0:
            dp[N] = (dp[N] + (-1 if x % 2 == 0 else 1) * dp[N - x*(3*x - 1)//2]) % mod

    N += 1

print('The value of n such that p(n) is divisible by 1 million: {0}'.format(N - 1))
