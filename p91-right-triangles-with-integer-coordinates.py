'''
To find the right triangles, iterate over all pairs of coordinates (x1, y1)
and (x2, y2). If (0,0), (x1, y1), (x2, y2) is not a degenerate triangle, 
we apply the dot product between each possible vector combination formed by
the coordinates. If the dot product is zero for any case, increase the total. 
Since each pair of coordinates is visited twice, the tally is halved to get
the final answer.
'''

ans = 0
mxn = 51
for x1 in range(0, mxn):
    for y1 in range(0, mxn):
        for x2 in range(0, mxn):
            for y2 in range(0, mxn):
                if x1 == 0 and y1 == 0: continue
                if x2 == 0 and y2 == 0: continue
                if x1 == 0 and x2 == 0: continue
                if y1 == 0 and y2 == 0: continue

                if x1 != x2 or y1 != y2: 
                    if (x2 - x1) * x1 + (y2 - y1) * y1 == 0:
                        ans += 1
                    if (x2 - x1) * x2 + (y2 - y1) * y2 == 0:
                        ans += 1
                    if x1 * x2 + y1 * y2 == 0:
                        ans += 1

print('The number of right triangles in the grid formed by \
0 <= x1, y1, x2, y2 <= 50: {0}'.format(ans // 2))