'''
For each number, split up the digits and add its factorials, and check if it is
saved in the dictionary. If so, then it signifies the start of a loop, and the
number of non repeating terms is the dictionary size so far. Add up all the instances
where the size is 60.
'''

fac = [1] + [x for x in range(1, 10)]
for x in range(1, 10):
    fac[x] *= fac[x - 1]

ans, mxn = 0, int(1e6) + 1
for x in range(3, mxn):
    memo = { x : True }
    while True:
        x = sum(fac[int(d)] for d in str(x))
        if x in memo:
            break
        memo[x] = True

    if len(memo) == 60:
        ans += 1

print('Number of terms less than one million with a chain length of 60: {0}'.format(ans))

