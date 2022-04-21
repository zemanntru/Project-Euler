'''
The Sieve of Eratosthenes is used up to two million. 
The resulting primes are added together.
'''

MXN = int(2e6)
prime = [True for i in range(MXN)]

p = 1
while (p*p <= MXN):
    p += 1
    if prime[p]:
        for i in range(p*p, MXN, p):
            prime[i] = False
   
ans = 0
for x in range(2, MXN):
    if prime[x] == True:
        ans += x

print('The sum of primes less than 2 million: {0}'.format(ans))