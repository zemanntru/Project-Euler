'''
Here, we take each irrational square root and expand it to a continued fraction 
of 200 iterations, which is more than enough to calculate the first 100 digits. Then,
this continued fraction is collapsed into a form n/d, and then it is manually divided
and the digit is saved at each stage of the division.
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

ans = 0
for n in range(2, 100):
    if int(math.sqrt(n)) != math.sqrt(n):
        mem, cons, stack = {}, [], []
        tup = next_iteration(n, int(math.floor(math.sqrt(n))), 1)
        mem[tup[0]] = [tup]
        stack.append(tup)
        cons.append(int(math.sqrt(n)))
        while True:
            tup = next_iteration(*tup[1:])
            if tup[0] not in mem:
                mem[tup[0]] = [tup]
            elif mem[tup[0]].count(tup) != 0:
                while len(stack) != 0:
                    top = stack.pop()
                    cons.append(top[0])
                    if top == tup:
                        break
                break
            else:
                mem[tup[0]].append(tup)

            stack.append(tup)  

        cons[1:] = reversed(cons[1:])
        cyc = cons[1:]
       
        while len(cons) <= 200:
            cons.extend(cyc)

        cons = cons[:201]
        pn, pd = cons[-1], 1
        for x in reversed(cons[:-1]):
            pn, pd = x * pn + pd, pn

        ans += pn // pd
        pn %= pd
        for x in range(99):
            ans += (pn * 10 // pd)
            pn = pn * 10 % pd
    
print('Sum of the first 100 digits of irrational square roots up to 100: {0}'.format(ans))