'''
The number of rectangles in a nxm grid is sum(1 <= j <= n)sum(1 <= k <= m)(n - j + 1)(m - k + 1)
which gives the close for S = mn(m + 1)(n + 1) / 4. Hence, the answer is min(abs(S(m,n) - 2000000)). 
Therefore it is sufficient to check through the values of m such that m*(m + 1) <= sqrt(8000000)
'''

import math

nRec = 2e6
ans, m, mna = 0, 1, 1e9

while math.pow(m*(m + 1), 2) <= 4 * nRec:
    n = int(math.sqrt(4.0 * nRec / (m * (m + 1))))
    da = abs(nRec - m*(m+1)*n*(n+1) / 4)
    if da < mna:
        mna = da
        ans = m*n

    m += 1

print('The area of the grid with the number of sub rectangles closest to 2 million is: {0}'.format(ans))