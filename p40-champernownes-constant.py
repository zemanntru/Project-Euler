'''
Here, we first find the number the xth digit is part of. A number whose largest
power of 10 is n contributes n + 1 digits. The number of digits consumed per decade
is 9n(n + 1). Once the correcth decade is identified, the remainder is used
to indentify which number it belongs to, and the specific digit.
'''

import math

def find_digit(x):
    if x < 10: return x
    s0, exp = 9, 1
    while True:
        s1 = s0 + (9 * (exp + 1) * math.pow(10, exp))
        if s1 > x: break
        s0 = s1
        exp += 1

    inc = math.pow(10, exp) + (x - s0 - 1) // (exp + 1)
    return int(str(inc)[int((x - s0 - 1) % (exp + 1))])

ans = find_digit(1) * find_digit(10) * find_digit(100) * find_digit(1000) * \
      find_digit(10000) * find_digit(100000) * find_digit(1000000)

print('product of the following digits: {0}'.format(ans))