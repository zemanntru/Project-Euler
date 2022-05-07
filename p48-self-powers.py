
'''
This approach makes use of binary exponentiation, where we gather and
multiply the exponent in intervals of powers of two mod 10^10 which speeds 
things up a lot. The answer is the sum of a^a using this process for 
1 <= a <= 1000
'''

mod = int(1e10)
def binexp(a, b):
    ret, a = 1, a % mod
    while b:
        if b & 1:
            ret = ret * a % mod
        a = a * a % mod
        b = b >> 1
    return ret

ans = sum(binexp(x, x) for x in range(1, 1001))
print('The last 10 digits of the series of powers: {0}'.format(ans % mod))
