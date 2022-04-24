'''
The Fibonacci numbers are added and once the 1000th digit is detected
record the index
'''
import math

f0, f1 = [0 for x in range(1200)], [0 for x in range(1200)]
f0[0], f1[0] = 1, 1

ans = 1
while f0[999] == 0:
    cbit, temp = 0, list(f1)
    for i in range(0, 1001):
        carry = 1 if f1[i] + f0[i] + cbit > 9 else 0
        f1[i] = (f1[i] + f0[i] + cbit) % 10
        cbit = carry
    f0 = temp
    ans += 1

print('The first 1000 digit Fibonacci number: {0}'.format(ans))