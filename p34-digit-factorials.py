''' 
We first find the upper bound for which numbers equal to the factorial sum of digits. 
Then, we loop through each individual number to check if it satisfies the condition
'''

from functools import reduce

digits = [x for x in range(1, 10)]
fac = [reduce(lambda x, y: x * y, digits[:x]) for x in range(1, 10)]
fac.insert(0, 1)

bnd, s0 = 9, fac[9]
while bnd < s0:
    bnd = bnd * 9 + 9
    s0 += fac[9]

ans = sum(x for x in range(10, s0) if x == sum(fac[i] for i in list(map(int, str(x)))))
print('The sum of all numbers equal to their digit factorial sums: {0}'.format(ans))
