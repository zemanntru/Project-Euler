'''
Through brute force, every feasible permutation of digits, operators and brackets is
generated. First [a,b,c,d] is generated, and each the combinations of three operators
is then inserted between each member of the quadruple permutation. Finally, brackets
are inserted into a$b$c$d where $ is an operator. Only two sets of brackets () are needed 
which covers all cases such as (a + b) * (c - d). There are two scenarios for the brackets:
either nested (()) or seperated ()(). All possible positions for the brackets is generated
for a$b$c$d, and the expression is evaluated, and saved in a dictionary if it's a positive
integer. Finally, for [a,b,c,d], the number of consecutive values 1,2...n is counted by looking
at the sorted keys of the dictionary, and abcd with the longest chain is the answer.
'''

from itertools import permutations

mxn, ans = 0, ''
opm = set(permutations(['+', '-', '*', '/', '+', '-', '*', '/', '+', '-', '*', '/'], 3))

for a in range(1, 7):
    for b in range(a + 1, 8):
        for c in range(b + 1, 9):
            for d in range(c + 1, 9):
                memo = {}
                for x in permutations([a, b, c, d], 4):
                    s = ''.join(map(str, x))
                    for op in opm:
                        s0 = s[0] + op[0] + s[1] + op[1] + s[2] + op[2] + s[3]
                        for x0 in range(0, 3):
                            for x1 in range(x0, 3):
                                for x2 in range(x1 + 1, 5):
                                    for x3 in range(x2, 5):
                                        s1 = s0[0:2*x0] + '(' + s0[2*x0:2*x1] + '(' + s0[2*x1:2*x2 - 1] + \
                                        ')' + s0[2*x2 - 1: 2*x3 - 1] + ')' + s0[2*x3 - 1:]
                                        try: val = eval(s1)
                                        except: pass
                                        else:
                                            if val > 0 and float(val).is_integer():
                                                memo[int(val)] = True

                        for x0 in range(0, 3):
                            for x1 in range(x0 + 1, 5):
                                for x2 in range(x1, 3):
                                    for x3 in range(x2 + 1, 5):
                                        s1 = s0[0:2*x0] + '(' + s0[2*x0:2*x1 - 1] + ')' + \
                                            s0[2*x1 - 1: 2*x2] + '(' + s0[2*x2: 2*x3 - 1] + ')' + s0[2*x3 - 1:]
                                        try: val = eval(s1)
                                        except: pass
                                        else:
                                            if val > 0 and float(val).is_integer():
                                                memo[int(val)] = True
                n = 1
                for x in sorted(memo.keys()):
                    if x != n:
                        if n > mxn:
                            mxn = n
                            ans = ''.join(map(str, [a, b, c, d]))

                        break

                    n += 1

print('The four distinct digits that produce the longest set of consecutive positive integers: {0}'.format(ans))