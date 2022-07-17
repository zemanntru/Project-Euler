'''
We iterate over all combinations of a and b and leveraging python's big integer to
add up all the digits. To reduce the work, the only viable candidates is if the maximum possible
digit sum is larger than the current maximum.
'''

import math

def ndig(a,b):
    return math.floor(1 + b*math.log10(a))

ans = 0
for a in range(99, 1, -1):
    for b in range(99, 1, -1):
        if 9*ndig(a,b) > ans:
            ans = max(ans, sum(map(int, str(a**b))))

print('The maximum digit sum is: {0}'.format(ans))