'''
This problem is quite similar to problem 9 in setting up the constraints. Refer to p9 for the boundary
analysis. We apply this process for p less than 1000, and count the number of solutions. The p with 
the most solutions is the answer.
'''

import math

ans, mxcnt = 0, 0
for x in range(5, 1000):
    cnt = 0
    for c in range(x // 3 + 1, x // 2):
        for a in range(1, c):
            if math.pow(a, 2) + pow(x - c - a, 2) == math.pow(c, 2):
                cnt += 1

    if cnt > mxcnt:
        mxcnt = cnt
        ans = x
            
print('The perimeter of the right triangle with the most solutions: {0}'.format(ans))