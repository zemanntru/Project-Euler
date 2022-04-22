'''
Create a dictionary with all necessary mappings, and for each number, 
parse it and lookup the numerical spelling. 

zero is used as a placeholder for an empty string
'''

ans = 0
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90]
words = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
          'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty',
          'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

lookup = dict(zip(num, words))
for n in range(1, 1000):
    if n < 20:
        ans += len(lookup[n])
    elif n < 100:
        ans += (len(lookup[n // 10 * 10]) + len(lookup[n % 10]))
    else:
        ans += (len(lookup[n // 100]) + len('hundred')) 
        n %= 100
        if 0 < n and n < 20:
            ans += (len('and') + len(lookup[n]))
        elif 0 < n and n < 100:
            ans += (len('and') + len(lookup[n // 10 * 10]) + len(lookup[n % 10]))

ans += (len('one') + len('thousand'))
print('character number of first 1000 numbers: {0}'.format(ans))
