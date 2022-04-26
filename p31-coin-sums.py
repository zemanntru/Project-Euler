'''
Let dp[n] be the number of ways to form n using the coins. Let k be the current denomination,
then dp[n] = dp[max(0, n - k)], where dp[n - k] represents all the way to form n - k with 
denominations up to k. If k = 10, then dp[n - 10] represents all the ways to form the value
n - 10 using 1, 2, 5 and 10s
'''

dp = [0 for x in range(0, 201)]
denom = [1, 2, 5, 10, 20, 50, 100, 200]

for x in denom:
    dp[x] += 1
    for i in range(2, 201):
        dp[i] += dp[max(0, i - x)]

ans = dp[200]
print('Number of ways to form 200p: {0}'.format(ans))

