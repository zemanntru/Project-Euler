'''
Solved via brute force. Iterate over every number less than one million and 
apply the collatz rule. Record the number with the maximum chain length.
'''
ans = 0
mxcnt = 0
collatz = lambda n: n / 2 if n % 2 == 0 else 3*n + 1

for n in range(2, 1000000):
    cnt = 0
    cur = n
    while cur != 1:
        cur = collatz(cur)
        cnt += 1

    if cnt > mxcnt:
        mxcnt = cnt
        ans = n

print('Number with the longest collatz chain: {0}'.format(ans))