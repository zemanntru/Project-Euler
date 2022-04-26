'''
Due to the limited range to check, a simple dictionary is used, and the
length of the map in the end is counted
'''
import math

memo = {}
for a in range(2, 101):
    for b in range(2, 101):
        res = int(math.pow(a, b))
        if res not in memo:
            memo[res] = True

print('number of distinct powers: {0}'.format(len(memo)))