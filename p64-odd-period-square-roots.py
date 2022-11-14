'''
suppose we have a fraction in form: (sqrt(a) - b0) / c0, then, what is the equivalent of:
1 / (p0 + (sqrt(a0) - b0) / c0)? by doing some algebra, we find c0 = (a - b^2) / c, a0 = a,
and b0 = -(b - p0 * c0) such that p0 is maximized in math.sqrt(a) + b - p0 * c0 > 0. 
Return the tuple of values for the next iteration. To find the cycles, each tuple is placed on a 
stack, and when the dictionary sees the exact tuple again, the number of times the stack is 
popped to find the tuple is the period
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
for n in range(2, 10001):
    if int(math.sqrt(n)) != math.sqrt(n):
        mem, stack, cyc = {}, [], 0
        tup = next_iteration(n, int(math.floor(math.sqrt(n))), 1)
        mem[tup[0]] = [tup]
        stack.append(tup)
        while True:
            tup = next_iteration(*tup[1:])
            if tup[0] not in mem:
                mem[tup[0]] = [tup]
            elif mem[tup[0]].count(tup) != 0:
                while len(stack) != 0:
                    cyc += 1
                    if stack.pop() == tup:
                        break
                break
            else:
                mem[tup[0]].append(tup)

            stack.append(tup)  
    
    ans += 1 if cyc % 2 == 1 else 0

print('Number of continued fractions for N <= 10000 that have an odd period: {0}'.format(ans))