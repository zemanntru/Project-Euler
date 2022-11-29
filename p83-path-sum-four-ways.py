'''
We use Dijkstra's algorithm since there is a set start and finish point. Given a number, 
treat each adjacent number as the edge to a new node. This is used to build an adjacency list,
and then the algorithm is applied, with the starting node being (0,0) and end node (79,79).
A minimal heap is used to speed up the process of reaching the end node.
'''

import heapq

mxn, mxL, a = 80, 1 << 60, []
adj, dp = {}, [[mxL] * mxn for x in range(mxn)]

infile = 'p83-path-sum-four-ways.in'
ss = open(infile).read().splitlines()
for ln in ss:
    a.append(list(map(int, ln.split(','))))

for i in range(mxn):
    for j in range(mxn):
        adj[(i,j)] = []
        if i > 0:
            adj[(i,j)].append((i - 1, j))
        if i + 1 < mxn:
            adj[(i,j)].append((i + 1, j))
        if j > 0:
            adj[(i,j)].append((i, j - 1))
        if j + 1 < mxn:
            adj[(i,j)].append((i, j + 1))

pq, ans = [], 0
heapq.heappush(pq, (a[0][0], (0,0)))
while len(pq) != 0:
    node = heapq.heappop(pq)
    if node[1] == (mxn - 1, mxn - 1):
        ans = node[0]
        break
    for n in adj[node[1]]:
        if node[0] + a[n[0]][n[1]] < dp[n[0]][n[1]]:
            dp[n[0]][n[1]] = node[0] + a[n[0]][n[1]]
            heapq.heappush(pq, (dp[n[0]][n[1]], n))

print('The minimal path sum from the top left to the bottom right is: {0}'.format(ans))