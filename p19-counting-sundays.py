'''
Since 365 mod 7 = 1 and 366 mod 7 = 2, the first day of a normal year will be one
weekday after the first day of the previous year, and two for leap years. Given Jan 1 1900
is on Monday, Jan 1 1901 is on Tuesday. The only century leap year concerned is 2000.
''' 
month = [x for x in range(1, 13)]
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
lookup = dict(zip(month, days))

ans, mod = 0, 2     # set for Tuesday
for n in range(1901, 2001):
    for m in range(1, 13):
        if mod == 0:
            ans += 1
        
        mod += lookup[m]
        if m == 2 and n % 4 == 0:
            mod += 1
        
        mod %= 7

print('Sundays on the first of the month in the twentieth century: {0}'.format(ans))