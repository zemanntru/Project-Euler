''' 
After some trial and error, the desired number has 12 digits. The upper and
lower bounds is established to narrow the search range. Here, the lower bound is
ceil(10^(11/3)) and upper bound floor(10^(12/3) - 1). Based on this, we compute
the cubes, and have nested for loops to count how many other cubes match the
permutation of the one being examined.
'''

from collections import Counter
import math

cubes = []
for x in range(4642, 9999):
    cubes.append(str(int(math.pow(x, 3))))

def compute():
    for i in range(0, len(cubes) - 1):
        cperm = 0
        for j in range(i + 1, len(cubes)):
            if Counter(cubes[i]) == Counter(cubes[j]):
                cperm += 1
            if cperm == 4:
                return cubes[i]

print('smallest cube for which exactly five permutations of its digits are cube: {0}'.format(compute())) 
            
