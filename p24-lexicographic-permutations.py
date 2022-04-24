'''
The permutation is found by swapping indices based on the largest factorial less than or equal to the
current iteration. Every time a swap is performed, subtract the largest such factorial from the
current iteration.

Take the example, [0, 1, 2, 3]: the 0th permutation is [0, 1, 2, 3], the 6th permutation is
[1, 0, 2, 3], and the 12th is [2, 0, 1, 3]. At each multiple of 3! = 6, we swap index 0 with index j,
where j = 1, and j = j + 1 after a swap. 

Suppose we want to find the 12th permutation (iteration = 12). At the 6th permutation, index 0 and 1 of 
[0, 1, 2, 3] is swapped to give [1, 0, 2, 3], and the iteration is now 6. Now, index 0 and 2 is swapped 
to give [2, 0, 1, 3], and the iteration is 0. 

If the iteration nonzero is less than the current factorial considered (say 3!), we move to the next index,
and apply this process recursively.
'''
import math, itertools

dig = [str(x) for x in range(0, 10)]
calc = [1]
ind, prod, nperm = 0, 1, 999999
ans = ''

for x in range(1,10):
    prod *= x
    calc.insert(0, prod)

while nperm > 0:
    cnt = ind + 1
    while nperm >= calc[ind]:
        dig[ind], dig[cnt] = dig[cnt], dig[ind]
        nperm -= calc[ind]
        cnt += 1
    ind += 1

print('Permuation one million is: ' + ans.join(dig))