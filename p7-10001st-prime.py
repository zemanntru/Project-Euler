''' 
We need to generate the Sieve of Eratosthenes to find the 10001st prime number.
The tricky thing is to find the size of the array to mark the primes.

The nth prime number, pn, is bounded by: pn < n(ln(n) + ln(ln(n)))
We find this upper bound and the rest is just the Sieve procedure.

Alternatively, you can just look up the 10001st prime...
'''
import math

sieve_upper = lambda x: x*(math.log(x) + math.log(math.log(x)))

MXN = int(sieve_upper(10001))
prime = [True for i in range(MXN)]

p = 1
while (p*p <= MXN):
    p += 1
    if prime[p]:
        for i in range(p*p, MXN, p):
            prime[i] = False
   
cnt = 0
for i in range(2, MXN):
    cnt += prime[i]
    if cnt == 10001:
        ans = i
        break


print('The 10001st prime number: {0}'.format(ans))