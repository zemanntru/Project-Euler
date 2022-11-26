'''
Through dynammic programming, denote F(i,j) as the minimum 
sum at the index (i,j) of the matrix, denoted M. Hence, this is 
cacluated as F(i,j) = M(i,j) + min(F(i - 1, j), F(i, j - 1)). The
answer is thus F(N - 1, N - 1) where N is the size of the matrix
'''

mxn = 80
a, dp = [], [[0] * mxn for x in range(mxn)]

infile = 'p81-path-sum-two-ways.in'
ss = open(infile).read().splitlines()
for ln in ss:
    a.append(list(map(int, ln.split(','))))

dp[0][0] = a[0][0]
for i in range(1, mxn):
    dp[0][i] += a[0][i] + dp[0][i - 1] 
    dp[i][0] += a[i][0] + dp[i - 1][0]

for i in range(1, mxn):
    for j in range(1, mxn):
        dp[i][j] = a[i][j] + min(dp[i - 1][j], dp[i][j - 1])

print('The minimal path sum to the bottom right corner of the matrix: {0}'.format(dp[mxn - 1][mxn - 1]))