'''
We use the pythagorean triple generator F(m,n) where the fundamental triples are in
the form a = m^2 - n^2, b = 2mn, and c = m^2 + n^2 where m > n > 0, m,n are integers.
This implies that F(k*(m,n)) = (k*a, k*b, k*c) are also triples. By the triangle inequality, 
c < a + b, so 2c < a + b + c <= 1500000, hence, c = m^2 + n^2 < m^2 < 750000,
giving an upper bound of m <= 866. Then for each 0 < n < m, all coprime pairs (m,n) 
will produce a right triangle of length L = 2m(m + n) < 1500000, which is then recorded. 
Furthermore, for all k such that k*L < 1500000 are also recorded. There exists values such that
F(k1*(m1,n1)) = F(k2*(m2,n2)), where the a and b values are swapped in each case. Hence, min(a,b)
is saved in a dictionary to avoid tallying the same triangle twice.
'''

import math

mxL = int(1.5e6)
mxm, Ln = int(math.sqrt(mxL / 2)), [0] * (mxL + 1)
memo = {}

for m in range(2, mxm + 1):
    for n in range(1, m):
        if math.gcd(m,n) == 1 and 2*m*(m + n) <= mxL:
            l, k = 2*m*(m + n), 1
            while k * l <= mxL:
                mn = k * min(m*m - n*n, 2*m*n)
                if k * l not in memo:
                    memo[k * l] = [mn]
                    Ln[k * l] += 1
                elif memo[k * l].count(mn) == 0:
                        memo[k * l].append(mn)
                        Ln[k * l] += 1
                k += 1
   
print('The number of values for L <= 1500000 which has one integer right sided triangle: {0}'.format(Ln.count(1)))
 

