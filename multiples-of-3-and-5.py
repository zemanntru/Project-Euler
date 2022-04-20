'''
The principle of inclusion and exclusion (PIE) is used. Sum all multiples of 3 from 0 to 1000,
then the multiples of 5 from 0 to 1000, and subtract the sum of multiples of 15 from 0 to 1000.
'''

MXN = 1000

# find the nth term for largest multiple less than 1000 of 3, 5, and 15
mul3 = int((MXN - 1) / 3)
mul5 = int((MXN - 1) / 5)
mul15 = int((MXN - 1) / 15)

# calculate the sums:
s3 = 3 * (1 + mul3) * mul3 / 2
s5 = 5 * (1 + mul5) * mul5 / 2
s15 = 15 * (1 + mul15) * mul15 / 2

#apply PIE
ans = s3 + s5 - s15

print("summation: " + str(int(ans)))
