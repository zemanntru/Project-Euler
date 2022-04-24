''' 
We do manual division for each number 2 < d < 1000, for each extension of a factor of 10,
we save it in a map and append it to a list. Once an extension is found again (found in the dictionary),
we backtrack by popping the list until the element is found again, and take the number of times pop is 
used. We save the d which gives the greatest period.
'''
ans, mxn = 0,0
for d in range(2, 1000):
    num, memo, div = 1, {}, []
    while num != 0: 
        if num < d:
            num *= 10
        if num in memo:
            cnt = 1
            while num != div.pop():
                cnt += 1
            if cnt > mxn:
                mxn = cnt
                ans = d
            break

        memo[num] = True
        div.append(num)
        num = num % d
        
print('The number less than 1000 that gives the greatest cyclic fraction: {0}'.format(ans))
    