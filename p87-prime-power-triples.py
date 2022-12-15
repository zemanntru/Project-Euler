'''
We first find all the prime numbers below sqrt(50 million) for the valid bases. Based
on that set of primes, take prime p, and place it in the p^2, p^3 and p^4 list assuming
p^n < 50 million. Then, we take all possible summations of the items in the three lists,
and mark all the sums as satisfying the property.
'''

import math

mxn = int(50e6)
smxn = int(math.sqrt(mxn)) + 1
psv, spn = [True] * smxn, [None] * mxn

lsp2, lsp3, lsp4 = [], [], []

p = 1
while p*p <= smxn:
    p += 1
    if psv[p]:
        for i in range(p*p, smxn, p):
            psv[i] = False

for p in range(2, smxn):
    if psv[p] == True:
        if math.pow(p, 2) < mxn:
            lsp2.append(int(math.pow(p, 2)))
        if math.pow(p, 3) < mxn:
            lsp3.append(int(math.pow(p, 3)))
        if math.pow(p, 4) < mxn:
            lsp4.append(int(math.pow(p, 4)))

for x2 in lsp2:
    for x3 in lsp3:
        for x4 in lsp4:
            if x2 + x3 + x4 < mxn:
                spn[x2 + x3 + x4] = True

print('Numbers under 50 million that are written as a sum of prime square, \
cube and fourth power: {0}'.format(spn.count(True)))