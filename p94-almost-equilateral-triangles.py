'''
By Heron's formula, s = 1/2(a + b + c) and A = sqrt(s*(s - a)*(s - b)*(s - c)). Let
the isoceles triangle be identified as (a, a, a - 1) or (a, a, a + 1). Plugging
this into Heron's formula gives 1/4*(a - 1)sqrt((3a - 1)*(a + 1)) and
1/4*(a + 1)sqrt((3a + 1)(a - 1)), which implies either (3a - 1)*(a + 1) = S^2 or 
(3a + 1)*(a - 1) = S^2. Completing the square gives: 3(a + 1/3)^2 - 4/3 = S^2 and
3(a - 1/3)^2 - 4/3 = S^2. Rearranging this gives ((3a + 1)/2)^2 - 3(S/2)^2 = 1 and
((3a - 1)/2)^2 - 3(S/2)^2 = 1. Substituting x = 3a + 1 or 3a - 1 and y = S/2 gives
the Pell equation x^2 - 3y^2 = 1. We know that the square root of 3 takes on form
[1,(1,2)], where the fraction x / y at the (n - 1)th element of the cycle is a solution
to the equation. Since n = 2 in this case, the starting point is '1' in the cycle, 
and whenever 1 is hit in the next cycle, evaluate the fraction, which the numerator
corresponds to either (3a + 1) / 2 or (3a - 1) / 2. Therefore, if 2*x mod 3 == 1 then
it is 3a + 1 otherwise 2*x mod 3 == 2 corresponds to 3a - 1. If 2*x is less than 1 billion,
tally it in the answer, assuming the perimeter does not correspond to a degenerate
triangle. (The only such case here is (1, 1, 0))
'''

mxL = int(1e9)

pn, pd = 1, 1
n, m = pn + pd, pn 
ans = 0

while 2*n < mxL:
    if 2*n // 3 > 2:
        ans += 2*n
    for x in [2, 1]:
        pn, pd = x * pn + pd, pn
    n, m = pn + pd, pn 
    
print('Sum of perimeters (P) of almost equilateral triangles integral areas and P \
satisfying P <= 1,000,000,000: {0}'.format(ans))