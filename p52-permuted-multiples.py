'''
The answer is a 6 digit number between 100000 and 167000. The lower limit is based on a 6 digit permutation requiring
a 6 digit number. The upper limit is to ensure the multiple of 6 does not overflow.
'''

ans = 0
for x in range(100000, 167000):
    bperm = True
    for n in [2,3,4,5,6]:
        bperm &= all(str(x).count(c) == str(x*n).count(c) for c in str(x))
    if bperm == True:
        ans = x
        break

print('the smallest number with a permuted multiple of 2-6 is: {0}'.format(ans))