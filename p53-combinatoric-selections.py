'''
With 23 <= x <= 100, calculate the first value n where the combination is greater that 
1 million. The last one is x - n, so the range of values is x - 2*n + 1.
'''

from math import comb

ans = 0
for x in range(23, 101):
    for n in range(3, x // 2):
        if comb(x, n) > 1000000:
            ans = ans + (x - 2*n + 1)
            break

print('Number of combinations with n <= 100 evaluating greater than 1 million: {0}'.format(ans))