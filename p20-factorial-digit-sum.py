'''
To obtain the large number factorial 100!, use manual multiplication, and store 
the resulting digits in a list. Finally, we take the resulting sum.
'''
import math

a = [0 for x in range(400)]
a[0] = 1

for i in range(2, 101):
    cbit = 0
    for j in range(0, 400):
        temp = (a[j]*i + cbit) // 10
        a[j] = (a[j]*i + cbit) % 10
        cbit = temp
    
print('digit sum of 100!: {0}'.format(sum(a)))