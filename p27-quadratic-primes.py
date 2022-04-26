
'''
We first set up the Sieve of Eratosthenes, and with the quadratic generator check if the consecutive
terms are marked. Record the quadratic function with the largest number of consecutive terms. Since it
begins with n = 0, this implies b is a prime, otherwise, f(0) is not a prime. For the case of n = 1, 
f(1) = a + b + 1, which implies -b < a < 1000.
'''

mxn = 10000000
prime = [True for i in range(mxn)]

p = 2
while (p*p <= mxn):
    if prime[p]:
        for i in range(p*p, mxn, p):
            prime[i] = False
    p += 1


mxlen, ans = 0, 0
for b in range(2, 1000):
    for a in range(-b + 1, 1000):
        cnt, func = 0, lambda x: x*x + a*x + b
        for n in range(0, 10000):
            if prime[func(n)]:
                cnt += 1
            else:
                if cnt > mxlen:
                    mxlen = cnt
                    ans = a*b
                break

print('The product of a and b for the largest chain of primes: {0}'.format(ans))

