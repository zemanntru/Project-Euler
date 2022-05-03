'''
We create a list of multiples for every divisor given. We start with a 3 digit
wide window on the last 3 digits. Then, apply recusion to slide the window to the
left by one spot if it satisfies our criteria until we have exhausted our list of 
divisors. Once all the divisors are exhausted, we find the missing first digit, and
add the current string of numbers to our answer.
'''

div = [{x*y : True for y in range(1, 999 // x + 1)} for x in [2,3,5,7,11,13,17]]

def calc(prev, ind, s0):
    if ind == -1:
        for x in range(0,10):
             if s0.find(str(x)) == -1:
                 s0 = str(x) + s0 
                 break

        return int(s0)

    accum = 0
    for cur in div[ind].keys():
        cur = str(cur) if cur >= 100 else '0' + str(cur)
        if len(set(cur)) == len(cur) and cur[1:] == prev[:-1] and s0.find(cur[0]) == -1:
            accum += calc(cur, ind - 1, cur[0] + s0)

    return accum

ans = 0
for cur in div[6].keys():
    cur = str(cur) if cur >= 100 else '0' + str(cur)
    if len(set(cur)) == len(cur):
        ans += calc(cur, 5, cur)

print('Sum of all 0 to 9 pandigital numbers satisfying the property: {0}'.format(ans))