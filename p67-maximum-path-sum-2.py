'''
This code is identical to problem 18, with a different text file

Our approach is dynammic programming: let index a[i][j] be the maximum total up to that point.
If the pyramid is n layers high, then max(a[n][j]) is the answer for 0 <= j < n
'''

a = []
infile = 'p67-maximum-path-sum-2.in'
ss = open(infile).read().splitlines()
for ln in ss:
    a.append(ln.split(' '))

dp = [[0 for j in range(len(a))] for i in range(len(a))]
dp[0][0] = int(a[0][0])

for i in range(1, len(a)):
    dp[i][0] = dp[i - 1][0] + int(a[i][0])
    for j in range(1, i + 1):
        dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + int(a[i][j])

ans = 0
for i in range(len(a)):
    ans = max(ans, dp[len(a) - 1][i])

print('The maximum path sum in the triangle is: {0}'.format(ans))