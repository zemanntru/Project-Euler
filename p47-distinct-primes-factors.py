'''
First, iterate over a range of numbers to count the number of distinct divisors save 
them into a list. Then, iterate over the range to count the first occurrence of 
four consecutive numbers with four divisors.
'''

def count_divisors(n):
    p, ret = 2, 0
    while n > 1:
        if n % p == 0:
            ret += 1
            while n % p == 0:
                n /= p
            
        if n == 1: break
        if p*p > n:
            ret += 1
            break
        p += 1
    return ret

mxn, cnt, ans = int(1e6), 0, 0
div = [0 for x in range(mxn)]
for x in range(2, mxn):
    div[x] = count_divisors(x)

for x in range(2, mxn):
    cnt = cnt + 1 if div[x] == 4 else 0
    if cnt == 4:
        ans = x - 3
        break

print('first of four consecutive numbers with 4 distinct prime factors: {0}'.format(ans))