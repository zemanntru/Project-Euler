'''
For each denominator, we find the upper and lower bounds for the numerator
that allows 1/2 < n/d < 1/3. Then, we loop over each numerator in the range,
and check if n and d are relatively prime
'''

import math

mxn, ans = 12001, 0

for d in range(2, mxn):
    lo = int(math.ceil((d + 1)/ 3))
    hi = int(math.ceil(d / 2))
    for x in range(lo, hi):
        if math.gcd(x, d) == 1:
            ans += 1

print('The number of reduced fractions between 1/3 and 1/2 for d <= 12000: {0}'.format(ans))