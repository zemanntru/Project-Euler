'''
Suppose we want to find the sum of the values on the nth spiral, which has a side length of
2n + 1. The sum of the four corners here are 4*(2n + 1)^2 - 2n - 2*2n - 3*2n
= 4*(2n + 1)^2 - 12*n. Repeat this for 1001 spirals
'''

ans = 1
mxn = (1001 - 1) // 2 + 1
for x in range(1, mxn):
    ans += (4*(2*x + 1)*(2*x + 1) - 12*x)

print('sum of diagonals in a 1001x1001 spiral: {0}'.format(ans))