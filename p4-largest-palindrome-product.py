'''
We iterate each number from 100 to 999 and multiply by some other 3 digit number. 
Then result is checked if it's a palindrome
'''

ans = 0

def is_palindrome(x):
    pal = [int(i) for i in str(x)]
    ret = True
    for i in range(0, int(len(pal) / 2)):
        ret &= (pal[i] == pal[-1 - i])

    return ret

for a in range(100, 1000):
    for b in range(100, 1000):
        if is_palindrome(a * b):
            ans = max(ans, a * b)

print('Largest Palindrome product made from two 3-digit numbers: {0}'.format(ans))


