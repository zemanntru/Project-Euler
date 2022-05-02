'''
The only pandigital numbers we consider are n = 4 and n = 7, since 
other values of n are guaranteed to be divisble by 3. In fact, we 
directly consider permutations of n = 7. From here, we generate the
permutations and test if they are prime.
'''

mxn, ans = 8000000, 0
prime = [True for i in range(mxn)]

def next_permutation(perm):
    for i in reversed(range(len(perm) - 1)):
        if perm[i] < perm[i + 1]:
            break
    else:
        return False

    for j in reversed(range(i + 1, len(perm))):
        if perm[i] < perm[j]:
            break

    perm[i], perm[j] = perm[j], perm[i]
    perm[i + 1:] = reversed(perm[i + 1:])
    return True

p = 1
while (p*p <= mxn):
    p += 1
    if prime[p]:
        for i in range(p*p, mxn, p):
            prime[i] = False

perm = [1, 2, 3, 4, 5, 6, 7]
while True:
    n = int(''.join(map(str,perm)))
    if prime[n] == True:
        ans = max(ans, n)

    if not next_permutation(perm):
        break

print('Largest pandigital prime number: {0}'.format(ans))