'''
The idea is to generate all permutations of [1,2,3,4,5,6,7,8,9], and
partition the result into three parts. Then check whether the first part multiplied
by the second part equals the third part. Then, save it in a dictionary and add up
the value of the keys at the end.
'''

def next_permutation(perm):
    for i in reversed(range(len(perm) - 1)):
        if perm[i] < perm[i + 1]:
            break
    else:
        return False

    for j in reversed(range(i + 1, len(perm))):
        if perm[i] < perm[j]:
            break

    perm[i], perm[j] = perm[j], perm[i]
    perm[i + 1:] = reversed(perm[i + 1:])
    return True

perm, memo = [1,2,3,4,5,6,7,8,9], {}

while True:
    for i in range(1, len(perm) - 1):
        for j in range(i + 1, len(perm) - i):
            a = int(''.join(map(str,perm[:i])))
            b = int(''.join(map(str,perm[i:j])))
            c = int(''.join(map(str,perm[j:])))
            if a*b == c:
                if c not in memo:
                    memo[c] = True

    if not next_permutation(perm):
        break

ans = 0
for prod in memo:
    ans += prod

print('sum of 9 digit pandigital products: {0}'.format(ans))