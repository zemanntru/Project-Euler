'''
Based on the triangle inequality, we have the constraint c < a + b < 2c, with 1000 - c = a + b.
Using these constraints, 334 < c < 500. let b = 1000 - c - a, so we need to find some a that 
satisfies: a^2 + (1000 - c - a)^2 = c^2, where a < c. 
'''

import math

ans = 0
for c in range(334, 500):
    for a in range(1, c):
        if math.pow(a, 2) + pow(1000 - c - a, 2) == math.pow(c, 2):
            ans = a * (1000 - c - a) * c
            break

print('pythagorean triple product abc: {0}'.format(ans))