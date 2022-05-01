'''
The Sieve of Eratosthenes is used up to create primes less than one million. 
For every prime that is visited, mark off each rotation so that if it is a circular prime,
we can skip checking any rotations of such number in the future
'''

import itertools
from collections import deque

mxn, ans = int(1e6), 0
prime, vis = [True for i in range(mxn)], [False for i in range(mxn)]

p = 1
while (p*p <= mxn):
    p += 1
    if prime[p]:
        for i in range(p*p, mxn, p):
            prime[i] = False


for i in range(2, mxn):
    if prime[i] and vis[i] == False:
        #deque is used for rotating the digits
        bcirc, dq, s0 = True, deque(map(int, str(i))), 0

        for j in range(0, len(dq)):
            perm = int(''.join(map(str, dq)))
            bcirc &= prime[perm]

            # this makes sure we do not overcount duplicate rotations
            if vis[perm] == False:
                s0 += 1

            vis[perm] = True
            dq.rotate()

        if bcirc == True:
            ans += s0

print('number of circular primes less than 1 million: {0}'.format(ans))

