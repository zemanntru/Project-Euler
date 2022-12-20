'''
The answer is solving n/(n + k) * (n - 1)/(n + k - 1) = 1/2. By some algebra, 
this is reduced to the quadractic equation k^2 + (2n - 1)nk + n - n^2, where
k = (1 - 2n + sqrt(8n^2 - 8n + 1)) / 2. Hence, for k to be an integer, 
8n^2 - 8n + 1 = S^2 for some integer S. By completing the square, the equation 
becomes S^2 - 2(2n - 1)^2 = -1, which is equivalent to the Pell equation
x^2 - 2y^2 = -1. The fundamental solution is (S, 2n - 1) = (1, 1), and the next solution (an,bn)
is attained by an + bn*sqrt(2) = (3 + 2sqrt(2))(an-1 + bn-1sqrt(2)), which gives
an = 3an-1 + 4bn-1, bn = 2an-1 + 3bn-1. Since k = (S + 1 - 2n) / 2, then n + k = (S + 1) / 2,
since x = S, the terminating condition is (x + 1) / 2 > 1e12 
'''

x, y = 1, 1
while x + 1 <= 2e12:
    x, y = 3*x + 4*y, 2*x + 3*y
        
print('The smallest number of blue discs inside a box with more \
 than a 10^12 chips: {0}'.format((y + 1) // 2))