'''
After extracting the roman numerals from the file, each character is parsed to generate
the decimal representation of the number. In the proper roman numeral for number N, the 
number of Ms correspond to floor(N / 1000). For the hundreds, tens and ones digit, each
follows the same casework but with different symbols. If the digit 0 <= d < 4, then the power
of 10 appears d times e.g (III, CC). However, for the special case of d = 4 then the 
subtraction rule is used e.g (IV, CM). The same argument is applied for d = 9, with
different symbols. Lastly, when 5 <= d < 9, the symbol for the half power of the next power of 10 
is appended (e.g V, L), and then the power of 10 symbol appears d - 5 times (e.g VI, DCC).
This new string is compared with the former roman numeral, and the difference in length is tallied
'''

infile = 'p89-roman-numerals.in'
ls_num = open(infile).read().split('\n')
ans = 0

for rnum in ls_num:
    num, ind, sz = 0, 0, len(rnum)
    while ind < sz:
        if rnum[ind] == 'M':
            num += 1000
        elif rnum[ind] == 'D':
            num += 500
        elif rnum[ind] == 'C':
            if ind + 1 < sz and rnum[ind + 1] == 'D':
                ind += 1
                num += 400
            elif ind + 1 < sz and rnum[ind + 1] == 'M':
                ind += 1
                num += 900
            else:
                num += 100
        elif rnum[ind] == 'L':
            num += 50
        elif rnum[ind] == 'X':
            if ind + 1 < sz and rnum[ind + 1] == 'L':
                ind += 1
                num += 40
            elif ind + 1 < sz and rnum[ind + 1] == 'C':
                ind += 1
                num += 90
            else:
                num += 10
        elif rnum[ind] == 'V':
            num += 5
        elif rnum[ind] == 'I':
            if ind + 1 < sz and rnum[ind + 1] == 'V':
                ind += 1
                num += 4
            elif ind + 1 < sz and rnum[ind + 1] == 'X':
                ind += 1
                num += 9
            else:
                num += 1

        ind += 1


    snum = 'M' * (num // 1000)
    num %= 1000
    if num // 100 < 4:
        snum += 'C' * (num // 100)
    elif num // 100 == 4:
        snum += 'CD' 
    elif num // 100 == 9:
        snum += 'CM'
    else:
        snum += 'D' + 'C' * (num // 100 - 5)

    num %= 100
    if num // 10 < 4:
        snum += 'X' * (num // 10)
    elif num // 10 == 4:
        snum += 'XL' 
    elif num // 10 == 9:
        snum += 'XC'
    else:
        snum += 'L' + 'X' * (num // 10 - 5)

    num %= 10
    if num < 4:
        snum += 'I' * num
    elif num == 4:
        snum += 'IV' 
    elif num == 9:
        snum += 'IX'
    else:
        snum += 'V' + 'I' * (num - 5)

    if rnum != snum:
        ans += abs(len(rnum) - len(snum))

print('The number of characters saved by writing roman numerals in minimal form: {0}'.format(ans))