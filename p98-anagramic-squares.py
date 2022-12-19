'''
After the list of words is read, the frequency count of each character in a word is tallied
in a 26 entry long list. To hash this list, it is converted into a 26-char string indicating the
count of each char and kept in a dict. The values of keys with more than two entries are kept,
and the maximum length mxd is taken. Then, valid squares are bounded by x^2 < 10^mxd, which
implies squares of x < sqrt(10^mxd) are generated. For each square, a similar frequency recording
procedure to the words is done, giving a list of lists containing squares that are anagrams.
Then, for each internal list, find string of the sorted raw count of distinct elements in the square,
for example, 41616 -> '122'. Based on this identifier, classify all squares satisfying this criteria
into the same group. Now for each pair of anagram words, The sorted raw count of distinct characters 
is taken similar to how it was done for the squares. This string is used as the key to the list
containing all possible squares that could match to this word. If both words have a match in the list,
the maximum of the two squares is taken.
'''

import math
from itertools import combinations

infile = 'p98-anagramic-squares.in'
words = list(map(lambda x: x.replace('"', ''), open(infile).read().split(',')))

def ind(x):
    return ord(x) - 65

mem_word = {}
for wd in words:
    freq = [0] * 26
    for c in wd: freq[ind(c)] += 1
    s0 = ''.join(map(str, freq))
    if s0 not in mem_word:
        mem_word[s0] = []

    mem_word[s0].append(wd)

anawd = list(filter(lambda x: len(x) > 1, mem_word.values()))
mem_sq = {}
for x in range(4, int(math.pow(10, len(max(anawd, key=lambda x: len(x[0]))[0]) / 2)) + 1):
    freq = [0] * 10
    for d in str(x*x): freq[int(d)] += 1
    s0 = ''.join(map(str, freq))
    if s0 not in mem_sq: 
        mem_sq[s0] = []

    mem_sq[s0].append(x*x)

anasq = list(filter(lambda x: len(x) > 1, mem_sq.values()))
anasqf = {}
for sq in anasq:
    freq = [0] * 10
    for x in str(sq[0]): freq[int(x)] += 1
    s0 = ''.join(map(str, sorted(filter(lambda x: x > 0, freq))))
    if s0 not in anasqf: 
        anasqf[s0] = []

    for s in sq: anasqf[s0].append(s)
    
ans = 0
for wd in anawd:
    freq = [0] * 26
    for x in wd[0]: freq[ind(x)] += 1
    idx = ''.join(map(str, sorted(filter(lambda x: x > 0, freq))))
    if idx in anasqf:
        for tup in combinations(wd, 2):
            for sq in anasqf[idx]:
                mems, valid = {}, True
                for i in range(len(tup[0])):
                    if tup[0][i] not in mems:
                        mems[tup[0][i]] = str(sq)[i]
                    elif mems[tup[0][i]] != str(sq)[i]:
                        valid = False
                
                s0 = int(''.join([mems[x] for x in tup[1]]))
                if valid and anasqf[idx].count(s0) != 0:
                    ans = max(ans, s0, sq)

print('The largest square given by any member of the anagram pair: {0}'.format(ans))

