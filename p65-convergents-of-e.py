'''
This problem is to evaluate the continued fraction. A list is used to store
all the constants to be added at each stage. To evaluate this, we solve the recurrence
at each stage: given a + b1/b2, the next stage would be b1 = a * b1 + b2, b2 = b1.
Then, add the digits of the numerator to get the final answer.
'''
cons, s0 = [1] * 100, 2

for x in range(2, 100, 3):
    cons[x], s0 = s0, s0 + 2

cons[0], pn, pd = 2, cons[-1], 1
for x in reversed(cons[:-1]):
    pn, pd = x * pn + pd, pn

print('The sum of the digits in the numerator of the 100th convergence of e: {0}'.format(sum(int(x) for x in str(pn))))