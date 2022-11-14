'''
This is solving the Pell equation by using the continued fractions method.
given x^2 - Dy^2 = 1, the minimal pair of solutions (x,y) would be the fraction p/q 
of sqrt(D) up to the n - 1 cycle for an even period of n or the 2n - 1 cycle for when
n is odd. The value of D that maximizes the value of p is the answer.
'''

import math

def next_iteration(a, b, c):
    s0 = math.sqrt(a) + b
    s1 = int((a - math.pow(b, 2)) / c)
    p0 = 0
    while s0 - s1 > 0:
        s0 -= s1
        b -= s1
        p0 += 1

    return (p0, a, -b, s1) 

mx, ans = 0, 0
for D in range(2,1001):
    if int(math.sqrt(D)) != math.sqrt(D):
        mem, stack = {}, []
        tup = next_iteration(D, int(math.floor(math.sqrt(D))), 1)
        mem[tup[0]], cons = [tup], [int(math.floor(math.sqrt(D)))]
        stack.append(tup)
        while True:
            tup = next_iteration(*tup[1:])
            if tup[0] not in mem:
                mem[tup[0]] = [tup]
            elif mem[tup[0]].count(tup) != 0:
                while len(stack) != 0:
                    cur = stack.pop()
                    cons.append(cur[0])
                    if cur == tup:
                        cons[1:] = cons[:0:-1]
                        if len(cons) % 2 == 0:
                            cons = cons + cons[1:]

                        cons = cons[:-1]
                        pn, pd = cons[-1], 1
                        for x in reversed(cons[:-1]):
                            pn, pd = x * pn + pd, pn

                        if pn > mx:
                            mx, ans = pn, D
                        break
                break
            else:
                mem[tup[0]].append(tup)
            stack.append(tup)  
    
print('the value of D <= 1000 in minimal solutions of x for which the largest value of x is: {0}'.format(ans))