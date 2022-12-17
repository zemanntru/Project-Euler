'''
The ord list records all pairs of numbers required to be on opposite sets (corresponding to the two cubes).
Then, all required faces satisfying these requirements is recursively generated as follows: let the input
be the two sets S1 and S2, and an index for the pair of numbers (a,b) for function F(S1, S2, i). The new 
pairs of sets is as follows: (S1 U a, S2 U b) and (S1 U b, S2 U a). If the bottom of the ord stack is reached, 
this terminates the recursion, return [(S1 U a, S2 U b), (S1 U b, S2 U a)] assuming distinct tuples. Otherwise,
return [F(S1 U a, S2 U b, i + 1), F(S1 U b, S2 U a, i + 1)] assuming distinct results. Then, the list (cub) 
of distinct  tuples (S1, S2) is converted into a string of numbers. Denote (S1, S2)(66) to indicate 6 is potentially 
present in both S1 and S2. To cover, the case of flipped 9s, we add elements (S1, S2)(69), (S1, S2)(96), (S1, S2)(99)
where (S1, S2)(96) is 6 flipped to 9 in S1 only, and stored in a master list (cub9). Then for each (S1, S2) in cub9,
if len(S) < 6, all legal arrangements is generated based on the existing S, giving L(S). Finally, for each possible
pair of strings s1, s2 between L(S1) and L(S2), they are hashed together to determine whether the pair is unique, 
corresponding to an unique arrangement of two cubes. s2 is then added to the list of strings compatible with s1, and
vice versa. The answer is the sum of the list corresponding to each valid 6-digit string. However, since the
ordering of the cubes does not matter the answer is divided by 2.
'''

import math

ord = [(0, 4), (0, 6), (1, 6), (1, 8), (2, 5), (3, 6), (4, 6)]

def GenCubSet(st1, st2, dep):

    rtup = []
    cs1a, cs1b = st1.copy(), st1.copy()
    cs2a, cs2b = st2.copy(), st2.copy()

    if st1.count(ord[dep][0]) == 0: 
        cs1a.append(ord[dep][0])

    if st2.count(ord[dep][0]) == 0: 
        cs2a.append(ord[dep][0])

    if st1.count(ord[dep][1]) == 0:
        cs1b.append(ord[dep][1])

    if st2.count(ord[dep][1]) == 0:
        cs2b.append(ord[dep][1])
    
    if max(len(cs1a), len(cs2b)) <= 6:
        rtup.append((cs1a, cs2b)) if dep == len(ord) - 1 else \
            rtup.extend(GenCubSet(cs1a, cs2b, dep + 1))

    if (cs1a != cs1b or cs2b != cs2a) and max(len(cs1b), len(cs2a)) <= 6:
        rtup.append((cs1b, cs2a)) if dep == len(ord) - 1 else \
            rtup.extend(GenCubSet(cs1b, cs2a, dep + 1))
    
    return rtup


cub = GenCubSet([0], [1], 0)
for i in range(len(cub)):
    cub[i] = (''.join(map(str, sorted(cub[i][0]))), \
              ''.join(map(str, sorted(cub[i][1]))))

cub9 = []
for tup in list(set(cub)):
    cub9.append(tup)
    if tup[0].count('6') != 0 and tup[1].count('6') != 0:
        cub9.append((''.join(map(str, sorted([int(x) for x in tup[0].replace('6', '9')]))), 
                     ''.join(map(str, sorted([int(x) for x in tup[1].replace('6', '9')])))))

    if tup[0].count('6') != 0:
        cub9.append((''.join(map(str, sorted([int(x) for x in tup[0].replace('6', '9')]))), tup[1]))

    if tup[1].count('6') != 0:
        cub9.append((tup[0], ''.join(map(str, sorted([int(x) for x in tup[1].replace('6', '9')])))))
      
def fillEmptyFaces(tup):
    if len(tup) == 6:
        return [tup]

    rtup = []
    for ds in ['0' * (6 - len(tup) - len(str(x))) + str(x) \
        for x in range(1, int(math.pow(10, 6 - len(tup))))]:
        if len(ds) == len(set(ds)) and sum(tup.count(str(d)) for d in ds) == 0: 
            rtup.append(tup + ''.join(map(str, ds)))

        for i in range(len(rtup)):
            rtup[i] = ''.join(map(str, sorted([int(x) for x in rtup[i]])))

    return list(set(rtup))

mem_cub = {}
for tup in cub9:
    tup0 = fillEmptyFaces(tup[0])
    tup1 = fillEmptyFaces(tup[1])
    for t0 in tup0:
        if t0 not in mem_cub:
            mem_cub[t0] = set()

        for t1 in tup1:
            if t1 not in mem_cub:
                mem_cub[t1] = set()

            mem_cub[t0].add(t1) 
            mem_cub[t1].add(t0)

print('The number of distinct arrangements of two cubes to form square numbers: \
{0}'.format( sum(len(x) for x in mem_cub.values()) // 2))
