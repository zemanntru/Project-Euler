'''
A triangular number is generated in the form n(n + 1)/2. If we prime factorize this number,
p1^n1 * p2^n2 * ... *pk^nk, then the number of divisors are (n1 + 1) * (n2 + 1) * ... * (nk + 1)
'''

# use a dict to track how many times a factor appears
def count_divisors(n):
    p = 2
    fac = {}
    while n > 1:
        if n % p == 0:
            cnt = 0
            while n % p == 0:
                n /= p
                cnt += 1
            fac[p] = cnt

        if n == 1: break

        if p*p > n:
            fac[n] = 1
            break

        p += 1

    ret = 1
    for p,n in fac.items():
        ret *= (n + 1)

    return ret

ans = 0
for n in range(1,1000000):
    if count_divisors(n*(n + 1)/2) > 500:
        ans = n*(n+1)/2
        break

print('First number with over 500 divisors: {0}'.format(ans))