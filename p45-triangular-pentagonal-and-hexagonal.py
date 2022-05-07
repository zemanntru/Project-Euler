'''
To see if the triangle number and pentagonal number has a match, we check that there is a 
positive integer solution to: 3n^2 - n - nt(nt + 1) = 0, where nt is the current term of the 
triangle number. Similarly, for the hexagonal case, there is a positive integer solution
to the following: 2n^2 - n - nt(nt + 1)/2 = 0
'''
import math

ans = 0
for t in range(286, 100000):
    vt = t * (t + 1) // 2
    np = (math.sqrt(1 + 24*vt) + 1) / 6
    nh = (math.sqrt(1 + 8*vt) + 1) / 4
    if np.is_integer() and nh.is_integer():
        ans = vt
        break

print('The next triangular number also a pentagonal and hexagonal number: {0}'.format(ans))