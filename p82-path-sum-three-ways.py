'''
For this problem, we move columwise from left to right. Let psa be
the prefix sum array of the current column, so psa[0] = 0 and psa[N] is
the sum of the entire column values. Let the current column index
be i and let 0,1,...N - 1 be the row-wise indices in the column
Hence, for 0 <= k <= m < j <= N, the minimal of dp[m][i] is between dp[m][i],
dp[k][i - 1] + sum(a[x][i] for k <= x <=m) and dp[j - 1][i - 1] + 
sum(a[x][i] for m <= x <= j). Finally, take the minimal of the values in the
rightmost column and that's the answer.
'''

mxL, mxn = 1 << 60, 80
a, dp, ans = [], [[mxL] * mxn for x in range(mxn)], mxL

infile = 'p82-path-sum-three-ways.in'
ss = open(infile).read().splitlines()
for ln in ss:
    a.append(list(map(int, ln.split(','))))

for i in range(0, mxn):
    dp[i][0] = a[i][0]

for i in range(1, mxn):
    psa = [0] * (mxn + 1)
    for j in range(1, mxn + 1):
        psa[j] += a[j - 1][i] + psa[j - 1]

    for j in range(2, mxn + 1):
        for k in range(j - 1):
            for m in range(k, j):
                dp[m][i] = \
                min(dp[m][i], \
                    dp[k][i - 1] + psa[m + 1] - psa[k], \
                    dp[j - 1][i - 1] + psa[j] - psa[m])

for i in range(mxn):
    ans = min(ans, dp[i][mxn - 1])

print('The minimal path sum from left to right: {0}'.format(ans))