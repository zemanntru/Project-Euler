'''
We want to set an upper bound to the numbers we want to explore. We keep adding power 9^5 until the
number formed by combining those digits exceed their sum. From there on, we just loop to that bound
and decompose the number to see if its a sum of fifth powers
'''
import math

num9, accum, ans = 9, math.pow(9, 5), 0

# establish the upper bound for search
while num9 < accum:
    num9 = num9 * 10 + 9
    accum += math.pow(9,5)
accum -= math.pow(9,5)                   

# repeatedly strip the last digit to form the power sum
for x in range(2, int(accum)):
    num, cnt = x, 0
    while num:
        cnt += math.pow(num % 10, 5)
        num //= 10
    if x == cnt:
        ans += x
        
print('The sum of all numbers that are written as a sum of fifth powers of digits: {0}'.format(ans))