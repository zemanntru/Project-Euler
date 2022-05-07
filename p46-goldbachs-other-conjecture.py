'''
We first use the Sieve of Eratosthenes to compute a list of primes to be checked.
Furthermore, we limit the range number of primes around 3000 so the the O(n^2) 
algorithm will not take too long. Then, we loop over all odd numbers less than the
maximal prime, and check if it satisfies the conjecture of not
'''

import math

sieve_upper = lambda x: x*(math.log(x) + math.log(math.log(x)))
mxn, plst, p, ans = int(sieve_upper(3000)), [], 1, 0
prime = [True for i in range(mxn)]

while (p*p <= mxn):
    p += 1
    if prime[p]:
        for i in range(p*p, mxn, p):
            prime[i] = False

for x in range(2, mxn):
    if prime[x]:
        plst.append(x)

for x in range(3, plst[-1], 2):
    if not prime[x]:
        p, conj = 0, False
        while plst[p] < x:
            if math.sqrt((x - plst[p])/2).is_integer():
                conj = True
                break
            p += 1
        
        if conj == False:
            ans = x
            break

print('First composite number that does not satisfy the conjecture: {0}'.format(ans))