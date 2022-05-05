'''
Here, we generate the pentagonal numbers and store them in a dictionary. 
Then, generate pairs of numbers and check if their sum and difference is
pentagonal. Note that the range is arbitrary set to the 5000th term since
we expect the value to be not large (as there's not an efficient way for me
to do it in less then O(n^2))
'''

pent = {int(x*(3*x - 1)/2) : True for x in range(1,10000)}

ans = 100000000
for i in range(2, 5000):
    for j in range(1, i):
        a = i*(3*i - 1) // 2
        b = j*(3*j - 1) // 2
        if a + b in pent and a - b in pent:
            ans = min(ans, a - b)

print('minimal pentagonal pair difference: {0}'.format(ans))