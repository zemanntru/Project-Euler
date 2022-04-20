'''
Iterate through each number from 2 to 20, and do prime factorization. Record the maximum number 
of times a factor appears in any of the numbers. The answer is the resulting product.
'''

factor = {}
ans = 1

def prime_factorize(x):

    p = 2
    while x > 1:
        if x % p == 0:
            cnt = 0
            if p not in factor:
                factor[p] = 0

            while x % p == 0:
                x /= p
                cnt += 1
            
            factor[p] = max(factor[p], cnt)

        if x == 1: 
            break

        if p*p > x:
            if x not in factor:
                factor[x] = 0

            factor[x] = max(factor[x], 1)
            break

        p += 1

for i in range(2, 21):
    prime_factorize(i)

for i,j in factor.items():
    ans *= pow(i, j)

print('Smallest multiple divisble by 1-20: {0}'.format(int(ans)))