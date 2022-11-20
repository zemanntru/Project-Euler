'''
For each denominator that is not a multiple of 7, we find the numerator that
gives the ratio of 3/7, and then round down the numerator. We keep subtracting
1 from the numerator so long as it is not relatively prime to the denominator.
Once the gcd(n, d) = 1, then we see which n/d pair gives the maximal value.
'''

from math import gcd

mxn, mxr, ans = int(1e6) + 1, 0, 0
for d in range(2, mxn):
    if d % 7 != 0:
        n = int(d * 3 / 7)
        while gcd(n, d) != 1:
            n -= 1
        if n / d > mxr:
            mxr, ans = n / d, n

print('The numerator of the fraction left to 3/7: {0}'.format(ans))
