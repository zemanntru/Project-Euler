'''
By taking the natural log of each number, then a^b becomes b*ln(a), which produces
a relatively small value that can be compared directly.
'''

import math

infile = 'p99-largest-exponential.in'
expls = open(infile).read().split('\n')
ln = lambda a, b : b * math.log(a)

ans, mxn = 0, 0
for i in range(len(expls)):
    mul = ln(*map(int, expls[i].split(',')))
    if mul > mxn:
        mxn = mul
        ans = i

print('The line containing the greatest exponential value: {0}'.format(ans + 1))

