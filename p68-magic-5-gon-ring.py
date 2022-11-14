'''
To ensure a 16 digit number, 10 is fixed on the outside node. Hence, we check the
remaining permutations from 1-9 and fill in the other circles, and take the 
maximum that satisfies the 5-gon property
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

perm, ans = [x for x in range(1, 10)], 0
while True:
    s0 = perm[0] + perm[4] + perm[5]
    s1 = perm[1] + perm[0] + perm[6]
    s2 = perm[2] + perm[1] + perm[7]
    s3 = perm[3] + perm[2] + perm[8]
    s4 = perm[4] + perm[3] + 10
    if all(s == s0 for s in [s1, s2, s3, s4]):
        mn, ind, res = 11, 0, ''
        for i in range(5, 9):
            if perm[i] < mn:
                mn, ind = perm[i], i

        for j in range(ind, ind + 5):
            res = res + (str(perm[j % 5 + 5]) if j != 9 else '10') + str(perm[(j + 4) % 5]) + str(perm[j % 5]) 

        ans = max(ans, int(res))
    if not next_permutation(perm):
        break

print('The maximum 16 digit string for 5-gon ring: {0}'.format(ans))