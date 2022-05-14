'''
The idea is to use the Sieve of Eratosthenes to find all primes under 1 million.
Then, create a prefix sum array of all the primes with the last element less
than 1 million. Then, find the two indices that maximise the difference, which 
is our answer
'''

mxn, p, ans = int(1e6), 1, 0
prime = [True for i in range(mxn)]
psa = []

while (p*p <= mxn):
    p += 1
    if prime[p]:
        for i in range(p*p, mxn, p):
            prime[i] = False

psa.append(2)
for x in range(3, mxn):
    if prime[x]:
        if x + psa[-1] < mxn:
            psa.append(x + psa[-1])
        else:
            break

ans = 0
for i in range(1, len(psa)):
    for j in range(0, i):
        if prime[psa[i] - psa[j]]:
            ans = max(ans, psa[i] - psa[j])

print('largest prime made of consecutive primes less than 1 million: {0}'.format(ans))