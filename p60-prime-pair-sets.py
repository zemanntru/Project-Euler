'''
Here, we visualize the primes as nodes in a graph. If two primes can be placed adjacently, then there
is an edge between the nodes. What we want to find is a set of five nodes forming a complete graph.
The first part is finding the primes via a sieve, then building the adjacency list. Once our edge connects two nodes
with a degree at minimum three, we can check if it forms a complete graph with 5 nodes. Therefore, we take shared nodes connecting
to the two nodes of interest for analysis. We then check the degree of these nodes. This list is then filtered to all nodes with
at least degree four, and if it is five or more, we test each subset of 5 nodes to see if it forms a complete graph
'''

from itertools import combinations

MXN = int(1e8)
prime = [True for i in range(MXN)]

p, prime[1] = 2, False
mem = {}
while (p*p <= MXN):
    if prime[p]:
        for i in range(p*p, MXN, p):
            prime[i] = False
    p += 1

def compute_task():
    adj, ans = {}, 0
    for x in range(2, MXN):
        if prime[x] == True:
            sn = str(x)
            for i in range(1, len(sn)):
                a = int(sn[0:i])
                b = int(sn[i:len(sn)])
                if str(a) == sn[0:i] and str(b) == sn[i:len(sn)] and \
                    prime[a] == True and prime[b] == True and \
                    prime[int(sn[i:len(sn)] + sn[0:i])] == True and a != b:
                        if a not in adj:
                            adj[a] = [b]
                        elif b not in adj[a]:
                            adj[a].append(b)
                        if b not in adj:
                            adj[b] = [a]
                        elif a not in adj[b]:
                            adj[b].append(a)
                            
                        if len(adj[a]) >= 3 and len(adj[b]) >= 3:
                            nodes = list(set([n for n in adj[a]]).intersection(set([n for n in adj[b]])))
                            nodes.append(a)
                            nodes.append(b)
                            vis = dict(zip(nodes, [0]*len(nodes)))
                            for n in nodes:
                                for m in adj[n]:
                                    if m in vis:
                                        vis[m] += 1
                    
                            cand = [n[0] for n in list(filter(lambda x: x[1] >= 4, vis.items()))]
                            if len(cand) >= 5:
                                for pent in list(combinations(cand, 5)):
                                    def isConn():
                                        for i in range(len(pent) - 1):
                                            for j in range(i + 1, len(pent)):
                                                if not adj[pent[i]].count(pent[j]):
                                                    return False
                                        return True
                                    if isConn() == True:
                                        return sum(pent)
    
                          
print('Lowest sum for a set of five primes satisfying the property: {0}'.format(compute_task())) 