'''
As usual, the Sieve of Eratosthenes is used to build a list of primes less than 1 million.
Then for each prime, each digit value is examined, and the number created by zeroing out 
that digit in the prime is stored in a dictionary. Then, the zero is replaced by one, two,
and so on to be checked whether it is still a prime. Possible answers occur when the count
is at least 8
'''

mxn, p, ans = int(1e6), 1, int(1e6)
prime = [True for i in range(mxn)]
memo = {}

while (p*p <= mxn):
    p += 1
    if prime[p]:
        for i in range(p*p, mxn, p):
            prime[i] = False

for x in range(2, mxn):
    if prime[x]:
        mdig = {}
        for c in str(x): 
            if c not in mdig:
                mdig[c] = True 

        for c in mdig:
            rep = str(x).replace(c, '0')
            if rep not in memo:
                memo[rep] = True
    
for rep in memo:
    cnt = 0
    for c in range(1, 10):
        if prime[int(rep.replace('0', str(c)))]:
            cnt += 1

    if cnt >= 8:
        for c in range(1, 10):
            cand = int(rep.replace('0', str(c)))
            if prime[cand]:
                ans = min(ans, cand)
                break

print('The smallest digit replacable prime part of a 8 member family: {0}'.format(ans))