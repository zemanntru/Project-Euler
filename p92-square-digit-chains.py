'''
For each number less than 10 million, continue adding the sum of the digit squares
until 1 or 89 is reached. This is then sped up using a cache to record whether N 
ends at 1 or 89, so that in future chains, if N is encountered after the summation, 
the loop can be be terminated.
'''

mxn, ans = int(1e7), 0
memo = {}
for cur in range(1, mxn):
    n = cur
    while not (cur == 1 or cur == 89):
        cur = sum(int(x)*int(x) for x in str(cur))
        if cur in memo:
            cur = memo[cur]

    memo[n] = cur
    if cur == 89:
        ans += 1

print('The number of starting numbers below 10 million that arrives at 89: {0}'.format(ans))