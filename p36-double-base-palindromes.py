'''
The approach is straightforward: convert the numbers into the string,
and compare half of the string with half of the string reversed, in
both base 2 and base 10
'''

mxn, ans = int(1e6), 0
for x in range(1, mxn):
    x10, x2 = str(x), bin(x)[2:]
    mid10, mid2 = len(str(x)) // 2, len(bin(x)[2:]) // 2
    if x10[:mid10] == x10[:-mid10 - 1:-1] and x2[:mid2] == x2[:-mid2 - 1: -1]: 
        ans += x

print('Sum of all base 2 and base 10 palindromes less than 1 million: {0}'.format(ans))
