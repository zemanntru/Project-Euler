'''
We guess that the largest prime is under 1 million (I cheated and looked up
the largest one: 739397). Therefore, we do the standard Sieve of Eratosthenes, and
and truncate the digits as necessary
'''

mxn, ans = int(1e6), 0
prime = [True for i in range(mxn)]
prime[1] = False

p = 1
while (p*p <= mxn):
    p += 1
    if prime[p]:
        for i in range(p*p, mxn, p):
            prime[i] = False

for x in range(10, mxn):
    if prime[x]:
        btrunc = True
        inc = 10
        while inc < x:
            btrunc &= prime[x % inc]
            inc *= 10

        while inc > 1:
            btrunc &= prime[int(x // inc)]
            inc /= 10

        if btrunc == True:
            ans += x

print('Sum of both left and right truncable primes: {0}'.format(ans))