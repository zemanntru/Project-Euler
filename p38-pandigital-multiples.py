'''
We can do some casework. Consider the cases for n:
n = 6: lower bound is 3, giving 3 1-digit number and 3 2-digit numbers,
       upper bound 3, however, 3 fails the pandigital requirement.
n = 5: one 1-digit number and 4 2-digit numbers. Possible multiple 
        4 < p < 10. Only viable choice here is p = 9, giving 918273645
n = 4: contains 3 2-digit numbers and one 3-digit number. Here, we obtain
        24 < p < 34
n = 3: contains 3 3-digit numbers. Here, the range is: 99 < p < 334

n = 2: contains a 4-digit number and 5-digit number. Here, the range is
       4999 < p < 10000

We form the string based on this casework, and check if the digits are unique
without the prescence of 0.
'''

ans = 918273645         # initial guess for n = 5

for x in range(25, 34):
    s0 = str(x) + str(x * 2) + str(x * 3) + str(x * 4)
    if len(set(s0)) == len(s0) and s0.find('0') == -1:
        ans = max(ans, int(s0))

for x in range(100, 334):
    s0 = str(x) + str(x * 2) + str(x * 3)
    if len(set(s0)) == len(s0) and s0.find('0') == -1:
        ans = max(ans, int(s0))

for x in range(5000, 10000):
    s0 = str(x) + str(x * 2)
    if len(set(s0)) == len(s0) and s0.find('0') == -1:
        ans = max(ans, int(s0))

print('Largest Pandigital multiple: {0}'.format(ans))