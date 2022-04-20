'''
Generate the all the fibonacci numbers less than 4 million. Store them in a list.
Then, iterate over the list and add all even numbers.
'''

MXFIBN = 4e6
ans = 0

f0, f1 = 0, 1
while f1 < MXFIBN:
    f0, f1 = f1, f0 + f1
    if(f0 % 2 == 0):
        ans = ans + f0

print('sum of even fibonacci numbers less than 4 million: {0}'.format(ans))
