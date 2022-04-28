'''
We generate all numbers greater than 10 not divisible by 10, and generate all numbers followed. 
Note that only the second digit of the numerator can be cancelled by the first digit of the denominator.
Multiply the four numerators and denominators, and take divide the denominator by their gcd at the end
to get the answer.
'''

import math

num, denom = 1, 1
for i in range(1, 10):
    for j in range(1, 10):
        cur = 10 * i + j
        for k in range(cur + 1, 100):
            if k % 10 != 0:
                ti = k // 10
                tj = k % 10
                if ti == j and  i / tj == cur / k:
                    num *= i
                    denom *= tj

ans = denom / math.gcd(num,denom)
print('Denominator of the product in lowest common terms: {0}'.format(int(ans)))