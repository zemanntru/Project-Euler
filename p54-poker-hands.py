hands = open('p54-poker-hands.in').read().replace('\n', ' ').split(' ')
sym = { '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
cons = '234567891011121314'
rflush = '1011121314'
ans = 0

def rank_hand(suits, val):
    memo = {}
    for x in val:
        if x not in memo:
            memo[x] = 1
        else:
            memo[x] += 1

    rnk = 0
    cnt = [x for x in memo.values()]
    if cnt.count(2) == 1:
        rnk = 1
    elif cnt.count(2) == 2:
        rnk = 2 
    if cnt.count(3) == 1:
        rnk = 3
    if ''.join(map(str, val)) in cons:
        rnk = 4
    if suits.count(suits[0]) == len(suits):
        rnk = 5
    if cnt.count(3) == 1 and cnt.count(2) == 1:
        rnk = 6
    if cnt.count(4) == 1:
        rnk = 7
    if ''.join(map(str, val)) in cons and suits.count(suits[0]) == len(suits):
        rnk = 8
    if ''.join(map(str, val)) in rflush and suits.count(suits[0]) == len(suits):
        rnk = 9

    return rnk

for n in range(0, len(hands) - 1, 10):
    a1, a2 = [x[1] for x in hands[n : n + 5]], [x[1] for x in hands[n + 5: n + 10]]
    b1, b2 = [sym[x[0]] for x in hands[n : n + 5]], [sym[x[0]] for x in hands[n + 5: n + 10]]
    b1.sort()
    b2.sort()

    r1 = rank_hand(a1, b1)
    r2 = rank_hand(a2, b2)
    if r1 > r2:
        ans += 1
    elif r1 == r2:
        if r1 == 0 and b1[-1] > b2[-1]:
            ans += 1
        elif r1 == 1:
            a1 = list(filter(lambda x : b1.count(x) == 2, b1))
            a2 = list(filter(lambda x : b2.count(x) == 2, b2))
            if a1[0] > a2[0]:
                ans += 1
            elif a1[0] == a2[0]:
                b1.remove(a1[0])
                b2.remove(a2[0])
                while b1:
                    if b1[-1] > b2[-1]:
                        ans += 1
                        break
                    elif b1[-1] < b2[-1]:
                        break
                    b1.pop()
                    b2.pop()
        elif r1 == 2:
            a1 = list(set(filter(lambda x : b1.count(x) == 2, b1)))
            a2 = list(set(filter(lambda x : b2.count(x) == 2, b2)))
            a1.sort()
            a2.sort()
            if a1[-1] > a2[-1]:
                ans += 1
            elif a1[-1] == a2[-1]:
                if a1[0] > a2[0]:
                    ans += 1
                elif a1[0] == a2[0]:
                    b1.remove(a1[0])
                    b1.remove(a1[1])
                    b2.remove(a2[0])
                    b2.remove(a2[1])
                    if b1[0] > b2[0]:
                        ans += 1

        elif r1 == 3:
            a1 = list(filter(lambda x : b1.count(x) == 3, b1))
            a2 = list(filter(lambda x : b2.count(x) == 3, b2))
            if a1[0] > a2[0]:
                ans += 1
            elif a1[0] == a2[0]:
                b1.remove(a1[0])
                b2.remove(a2[0])
                while b1:
                    if b1[-1] > b2[-1]:
                        ans += 1
                        break
                    elif b1[-1] < b2[-1]:
                        break
                    b1.pop()
                    b2.pop()

        elif r1 == 4 and b1[-1] > b2[-1]:
            ans += 1
        elif r1 == 5 and b1[-1] > b2[-1]:
            ans += 1
        elif r1 == 6:
            a1 = list(filter(lambda x : b1.count(x) == 3, b1))
            a2 = list(filter(lambda x : b2.count(x) == 3, b2))
            if a1[0] > a2[0]:
                ans += 1
            elif a1[0] == a2[0]:
                b1.remove(a1[0])
                b2.remove(a2[0])
                if b1[-1] > b2[-1]:
                    ans += 1
        elif r1 == 7:
            a1 = list(filter(lambda x : b1.count(x) == 4, b1))
            a2 = list(filter(lambda x : b2.count(x) == 4, b2))
            if a1[0] > a2[0]:
                ans += 1
            elif a1[0] == a2[0]:
                b1.remove(a1[0])
                b2.remove(a2[0])
                if b1[-1] > b2[-1]:
                    ans += 1

        elif r1 == 8 and b1[-1] > b2[-1]:
            ans += 1

print('The number of times player 1s hand wins: {0}'.format(ans))