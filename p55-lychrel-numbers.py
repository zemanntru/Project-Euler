'''
Here, for every number less than 10000 we do at most 50 iterations of adding the reverse 
number, and check whether it is a palindrome
'''

ans = 9999
for x in range(1, 10000):
    for j in range(0, 50):
        x = x + int(''.join(reversed(str(x))))
        mid = len(str(x)) // 2
        if str(x)[:mid] == str(x)[:-mid - 1:-1]:
            ans -= 1
            break

print('Number of Lychrel numbers less than 10000: {0}'.format(ans))