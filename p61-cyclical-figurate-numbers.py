'''
We can treat the two adjacent digits together as a node. In a four digit number, there is a directed edge
from the node represented by the first two digits to the node represented by the last two digits, and the
transition between the geometrical type (i.e triangle to pentagonal). Then, this problem becomes building the graph, 
and finding a subgraph that is a cycle of depth 6. This is done using a depth first search. We also use a dictionary to make 
sure the transition between geometries is unique.
'''

adj = {}
check = [[] for n in range(6)]
for n in range(45, 141):
    sn = str(int(n*(n + 1)/2))
    check[0].append(int(sn))
    if str(int(sn[0:2])) == sn[0:2] and \
        str(int(sn[2:4])) == sn[2:4]:
        if sn[0:2] not in adj:
            adj[sn[0:2]] = []
        adj[sn[0:2]].append((sn[2:4], 0))

for n in range(32, 100):
    sn = str(int(n*n))
    check[1].append(int(sn))
    if str(int(sn[0:2])) == sn[0:2] and \
        str(int(sn[2:4])) == sn[2:4]:
        if sn[0:2] not in adj:
            adj[sn[0:2]] = []
        adj[sn[0:2]].append((sn[2:4], 1))

for n in range(26, 82):
    sn = str(int(n*(3*n - 1)/2))
    check[2].append(int(sn))
    if str(int(sn[0:2])) == sn[0:2] and \
        str(int(sn[2:4])) == sn[2:4]:
        if sn[0:2] not in adj:
            adj[sn[0:2]] = []
        adj[sn[0:2]].append((sn[2:4], 2))

for n in range(23, 71):
    sn = str(int(n*(2*n - 1)))
    check[3].append(int(sn))
    if str(int(sn[0:2])) == sn[0:2] and \
        str(int(sn[2:4])) == sn[2:4]:
        if sn[0:2] not in adj:
            adj[sn[0:2]] = []
        adj[sn[0:2]].append((sn[2:4], 3))

for n in range(21, 64):
    sn = str(int(n*(5*n - 3)/2))
    check[4].append(int(sn))
    if str(int(sn[0:2])) == sn[0:2] and \
        str(int(sn[2:4])) == sn[2:4]:
        if sn[0:2] not in adj:
            adj[sn[0:2]] = []
        adj[sn[0:2]].append((sn[2:4], 4))

for n in range(19, 59):
    sn = str(int(n*(3*n - 2)))
    check[5].append(int(sn))
    if str(int(sn[0:2])) == sn[0:2] and \
        str(int(sn[2:4])) == sn[2:4]:
        if sn[0:2] not in adj:
            adj[sn[0:2]] = []
        adj[sn[0:2]].append((sn[2:4], 5))


for nodes in adj.keys():
    vis = {}
    res = []
    def dfs(ref, node, dep, mem):
        if dep == 6:
            return 1 if node == ref else 0
            
        if node in vis:
            return 0

        vis[node] = True
        for pv in adj[node]:
            if pv[1] not in mem:
                mem2 = mem.copy()
                mem2[pv[1]] = True
                ret = dfs(ref, pv[0], dep + 1, mem2) 
                if ret != 0:
                    res.append(int(node + pv[0]))
                    return int(node + pv[0])

        return 0 
    
    if dfs(nodes, nodes, 0, {}) != 0:
        ans = sum(res)
        break

print('Sum of the ordered set of six cyclic 4-digit numbers: {0}'.format(ans)) 