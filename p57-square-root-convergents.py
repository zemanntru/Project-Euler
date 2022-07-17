'''
assume the fraction from the last iteration is a/b. Then, the next iteration would be the
fraction  1 + 1/(1 + a/b) = a + 2*b / a + b. Thus, an = an-1 + 2*bn-1, bn = an-1 + bn-1. 
Thus, we check if the length of the numerator is greater than the denominator and count
all the occurrences
'''

a, b, ans = 1, 1, 0
for x in range(0, 1000):
    a, b = a + 2*b, a + b
    if len(str(a)) > len(str(b)):
        ans += 1

print('The number of expansions where the numerator contains more digits than the denominator: {0}'.format(ans))