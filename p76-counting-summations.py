'''
We add up all the partitions for n into k parts for 1 < k < 100.
A cache is used to speed up the process.
'''

dp = [[None] * 101 for x in range(101)]
def f(n, k):
    if dp[n][k] != None:
        return dp[n][k]

    if n < k:
        return 0
    elif n == k or k == 1:
        return 1
   
    dp[n][k] = f(n - 1, k - 1) + f(n - k, k)
    return dp[n][k]

print('Number of ways to partition 100 into two \
or more parts: {0}'.format(sum(f(100, k) for k in range(2, 101))))

