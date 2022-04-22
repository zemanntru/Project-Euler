'''
Assume the product is less than 400 digits. Initialize an array of that length
to store the digits. Now, multiply 1000 times and get the resulting big number
in the array. Finally, sum the resulting digits
'''

import math

a = [0 for x in range(400)]
a[0] = 1

for i in range(1000):
    cbit = 0
    for j in range(0, 400):
        temp = (a[j]*2 + cbit) // 10
        a[j] = (a[j]*2 + cbit) % 10
        cbit = temp
    
print('sum of digits of 2^1000: {0}'.format(sum(a)))
        
