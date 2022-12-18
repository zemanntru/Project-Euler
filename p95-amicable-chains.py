'''
This problem is solved mainly through brute force. Given n, it is prime factorized
and the sum of the proper divisors is sum((pk^(ek + 1) - 1) / (pk - 1)) - n over all
k prime factors. There are three cases for this sum: either it will diverge or converge
to 1, or get stuck in a chain. Therefore, n is invalid if the sum is greater than 1 million 
or is 1. In the case n is saved in the dictionary, it is skipped entirely. If the sum reaches
a member of an amicable chain of the first time, all members in the chain amicable chain will
marked in the dictionary, and any future references to them are skipped. To distinguish non member
numbers, a stack is used: if a number is encountered twice on the stack, all numbers in
between are part of the chain, and the length of the chain and minima is compared.
'''

import math

mxn = int(1e6)
mxL, ans = 0, 0
mem_amc = {}

def calc_amicable(x):
    if x in mem_amc: return None
    p = 2          
    mem_fac, n = {}, x        
    while n > 1:
        if n % p == 0:
            mem_fac[p] = 0
            while n % p == 0:
                n //= p
                mem_fac[p] += 1
        if n == 1: break
        if p*p > n:
            mem_fac[n] = 1
            break

        p += 1 if p == 2 else 2

    mul = 1
    for p, e in mem_fac.items():
        mul *= int(math.pow(p, e + 1) - 1) / (p - 1)

    sumf = mul - x
    if sumf == 1 or sumf > mxn:
        mem_amc[x] = None
        return None

    return sumf

for x in range(2, mxn):
    mem = { x : True }
    stack = [x]
    while True:
        x = calc_amicable(x)
        if x == None: break
        stack.append(x)
        if x not in mem:
            mem[x] = True
        else: 
            cnt, mn = 0, mxn
            stack.pop()
            while len(stack) != 0:
                cur = stack.pop()
                mn = min(mn, cur)   
                mem_amc[cur] = None
                cnt += 1
                if x == cur: break

            while len(stack) != 0:
                cur = stack.pop()
                mem_amc[cur] = None

            if cnt > mxL:
                mxL, ans = cnt, mn

            break
    
    
print('The smallest member of the longest amicable chain with \
all elements less than 1 million: {0}'.format(ans))