'''
We check over all four digit numbers, and generate triplets of the digit
shuffled. If the condition is satisfied, save it in a dictionary.
'''

from itertools import combinations, permutations

mxn, p = int(1e5), 1
prime = [True for i in range(mxn)]
ans = {}

while (p*p <= mxn):
    p += 1
    if prime[p]:
        for i in range(p*p, mxn, p):
            prime[i] = False

for x in range(1000, 10000):
    if prime[x]:
        perm = list(permutations(map(int, str(x)), 4))
        for triple in set(combinations(perm, 3)):
            x1 = int(''.join(map(str, triple[0])))
            x2 = int(''.join(map(str, triple[1])))
            x3 = int(''.join(map(str, triple[2])))
            if x3 > x2 and x2 > x1 and prime[x1] and prime[x2] and prime[x3] and x2 - x1 == x3 - x2:
                ss = str(x1) + str(x2) + str(x3)
                if ss not in ans:
                    ans[ss] = True
                    
for x in ans:
    print('concatenated number of possible solution: {0}'.format(x))
