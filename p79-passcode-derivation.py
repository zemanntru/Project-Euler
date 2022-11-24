'''
Since the digits are always in order, this means that the passcode
consists of unique digits. Hence, we track the index of each digit.
For every attempt, look at the pair of consecutive digits. If the index
of the first is larger than the second, swap the indices.
'''

infile = 'p79-passcode-derivation.in'
pwd = open(infile).read().split('\n')[:-1]

idx, tail, memo = [0]*10, 0, {}

for cv in pwd:
    pr = -1
    for x in cv:
        if int(x) not in memo:
            memo[int(x)] = True
            idx[int(x)] = tail
            tail += 1
            continue

        if pr != -1 and idx[pr] > idx[int(x)]:
            idx[pr], idx[int(x)] = idx[int(x)], idx[pr]
            
        pr = int(x)

ans = []
for a in range(0, 10):
    for b in range(0, 10):
        if b in memo and a == idx[b]:
            ans.append(b)

print('The shortest possible password: {0}'.format(''.join(map(str, ans))))

