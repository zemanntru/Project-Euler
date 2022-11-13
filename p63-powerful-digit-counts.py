'''
for a number with n digits that is also in a form x^n, the lower bound of x would be l = ceil(10^(x/(x+1))),
hence, l <= x < 10, where x is an integer. Therefore, the upper limit of n would yield l = 10. Hence, we get
the equation 10^(x/(x + 1)) < 9. Solving, this, we see x <= 20. Therefore, we sum all the possible values in
range of 1 <= x <= 20, then add 9 for the case of 1-9.
'''
import math

ans = 9 + sum(10 - math.ceil(math.pow(10, x/(x + 1))) for x in range(1, 21))

print('Number of n-digit positive integers exist which are also an nth power: {0}'.format(ans))