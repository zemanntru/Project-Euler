
'''
Through binary exponentiation, and taking modulo 10 billion at each step, 
it provides a quick and anti-integer overflow method of computing.
''' 

MOD = int(1e10)
a, b, mul = 2, 7830457, 1
while b > 0:
    if b & 1:
        mul = mul * a % MOD
    a = a * a % MOD
    b >>= 1

print('The last ten digits of 28433 * 2^7830457 + 1: {0}'.format((28433 * mul + 1) % MOD))