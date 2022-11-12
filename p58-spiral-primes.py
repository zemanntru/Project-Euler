'''
Using 1 billion as the loose upper bound. Create a sieve and then mark the primes.
Then, count the primes on the spiral corners and break when the ratio crosses
the threshold
'''

import math

MXN = int(1e9)
prime = [True for i in range(MXN)]

p, pct, ans = 1, 0, 0
while (p*p <= MXN):
    p += 1
    if prime[p]:
        for i in range(p*p, MXN, p):
            prime[i] = False


for n in range(1, int(math.sqrt(MXN) / 2 - 1)):
    pct += 1 if prime[(2*n + 1)*(2*n + 1) - 2*n] else 0
    pct += 1 if prime[(2*n + 1)*(2*n + 1) - 4*n] else 0
    pct += 1 if prime[(2*n + 1)*(2*n + 1) - 6*n] else 0
    if pct / (4*n + 1) < 0.1:
        ans = 2*n + 1
        break

print('The first spiral where the ratio of primes is less than 10%: {0}'.format(ans))