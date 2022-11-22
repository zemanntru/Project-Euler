sfac = [0] * 2
def sumfac(x):
    if x < len(sfac):
        return sfac[x]

    sfac.append(0)
    if x == len(sfac):
        print(x, len(sfac))
        assert False

    n, p, ret = x, 2, 0
    while n > 1:
        if n % p == 0:
            sfac[x] += p
            while n % p == 0:
                n /= p

        if n == 1: break
        if p*p > n:
            sfac[x] += n
            break
        p += 1

    return sfac[x]