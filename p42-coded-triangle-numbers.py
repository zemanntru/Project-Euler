'''
This problem is solved via direct computation. First, we generate a dictionary
of triangular numbers. Enter each word into a list, convert each letter into its char value 
and subtract 64 (since 'A' is 65). Add up the char values to see if it's in the dictionary,
and if so, increment the answer by one.
'''

infile = 'p42-coded-triangle-numbers.in'
words = open(infile).read().split(',')

tri = {int(x*(x + 1)/2) : True for x in range(1, 100)}

ans = 0
for x in range(len(words)):
    if sum(ord(c) - 64 for c in words[x][1:-1]) in tri:
        ans += 1

print('Number of triangular words in the file: {0}'.format(ans))