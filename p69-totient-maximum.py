'''
The totient function is generated through 
phi(m) = m(1 - 1/p1)(1 - 1/p2)...(1 - 1/pk), there therefore,
m/phi(m) = p1/(p1 - 1)p2/(p2 - 1)...pk/(pk - 1). The algorithm 
is to find all prime factors of m, and then apply the multiplication
'''

from functools import reduce

def factor(x):
    p, ret = 2, 1
    while x > 1:
        if x % p == 0:
            ret *= p / (p - 1)
            while x % p == 0:
                x /= p
        if x == 1: 
            break
        if p*p > x:
            ret *= x / (x - 1)
            break
        p += 1
    return ret

ans, mx = 0, 0
for n in range (2, 1000001):
    cur = factor(n)
    if cur > mx:
        mx, ans = cur, n

print('The largest ratio of n to phi(n): {0}'.format(ans))