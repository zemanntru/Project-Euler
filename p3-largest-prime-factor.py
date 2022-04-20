'''
We iterate through all numbers below the sqrt(600851475143) which is 
around 3 million. This is small enough to check each number individually
'''

# start at 3, we see that the number is not even
MXN = 600851475143
p = 3                       
ans = 0

while MXN > 1:
    if MXN % p == 0:
        while MXN % p == 0:
            MXN /= p
        ans = max(ans, p)
        
    if p*p > MXN:
        ans = max(ans, MXN)
        break

    p += 2

print('largest prime factor: {0}'.format(int(ans)))