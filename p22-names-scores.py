'''
This problem is solved via direct computation. Enter each name into a list,
convert each letter into its char value and subtract 64 (since 'A' is 65).
Add up the char values and multiply by its position
'''

infile = 'p22-names-scores.in'
names = open(infile).read().split(',')
names.sort()
ans = 0
for x in range(len(names)):
    cnt = 0
    for c in names[x][1:-1]:
        cnt += (ord(c) - 64)
    ans += (x + 1)*cnt

print('score of all names combined: {0}'.format(ans))