''' 
This is solved via direct computation. The closed forms for each series are:

1^2 + 2^2 + ... + n^2 = n(n+1)(2n+1)/6

1 + 2 + 3 + ... + n = n(n+1)/2

So we want to find: n^2(n+1)^2/4 - n(n+1)(2n+1)/6

Simplifying gives the closed form: n(n+1)(3n^2 - n - 2)/12
'''

def compute_diff(n):
    return n*(n+1)*(3*n*n - n - 2)/12

ans = compute_diff(100)

print('difference: {0}'.format(int(ans)))