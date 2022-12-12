'''
This problem involves building a probability matrix and repeatedly multiplying a probability 
vector. For each tile there are three states: for none, one and two doubles rolled so far. 
For each square on the board, we calculate the probability of all the possible locations that 
can be reached and their respective states, and save it in the matrix. The special cases are
the (go to) jail square and the chance and community chance squares, and the new reachable locations
and their probabilities are saved in a list
'''


sq = ['GO', 'A1', 'CC', 'A2', 'T1', 'R1', 'B1', 'CH', \
       'B2', 'B3', 'G2J', 'C1', 'U1', 'C2', 'C3', 'R2', \
       'D1', 'CC', 'D2', 'D3', 'FP', 'E1', 'CH', 'E2', \
       'E3', 'R3', 'F1', 'F2', 'U2', 'F3', 'G2J', 'G1', \
       'G2', 'CC', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2']

adj = [[0.0] * 120 for x in range(120)]
vprob = [1.0] + [0.0] * 119

cG0, cR1, c2J, cC1, cU1, cE3, cU2, cH2 = 0, 5, 10, 11, 12, 24, 28, 39

def pack(x, y):
    return 3*x + y

def next_R(x):
    return (x + 5) % 40 // 10 * 10 + 5

def next_U(x):
    return cU2 if 13 < x and x < 28 else cU1

def next_ind_prob(x, dx):
    ind = (x + dx) % 40
    if sq[ind] == 'CC':
        return [(cG0, 1.0 / 16), (c2J, 1.0 / 16), (ind, 14.0 / 16)]
    elif sq[ind] == 'CH':
        return [(cG0, 1.0 / 16), (c2J, 1.0 / 16), (cC1, 1.0 / 16), (cE3, 1.0 / 16), \
                (cH2, 1.0 / 16), (cR1, 1.0 / 16), (next_R(ind), 1.0 / 8), \
                (next_U(ind), 1.0 / 16), (ind, 6.0 / 16), (ind - 3, 1.0 / 16)] 
    elif sq[ind] == 'CH3':
        return [(cG0, 1.0 / 16), (c2J, 1.0 / 16), (cC1, 1.0 / 16), (cE3, 1.0 / 16), \
                (cH2, 1.0 / 16), (cR1, 1.0 / 16), (next_R(ind), 1.0 / 8),
                (next_U(ind), 1.0 / 16), (ind, 6.0 / 16), (cG0, 1.0 / 256), (c2J, 1.0 / 256), (ind - 3, 14.0 / 256)]
    elif sq[ind] == 'G2J':
        return [(c2J, 1.0)]
    else:
        return [(ind, 1.0)]

def markov_builder_2_die6f():
    for sq in range(40):
        for ind, prob in next_ind_prob(sq, 2):
            adj[pack(ind, 1)][pack(sq, 0)] += 1.0 * prob / 36         # rolls double 1, no double so far
            adj[pack(ind, 2)][pack(sq, 1)] += 1.0 * prob / 36         # rolls double 1, one double so far

        for ind, prob in next_ind_prob(sq, 3):
            adj[pack(ind, 0)][pack(sq, 0)] += 2.0 * prob / 36         
            adj[pack(ind, 0)][pack(sq, 1)] += 2.0 * prob / 36
            adj[pack(ind, 0)][pack(sq, 2)] += 2.0 * prob / 36
        
        for ind, prob in next_ind_prob(sq, 4):
            adj[pack(ind, 0)][pack(sq, 0)] += 2.0 * prob / 36         # case for non double roll
            adj[pack(ind, 0)][pack(sq, 1)] += 2.0 * prob / 36
            adj[pack(ind, 0)][pack(sq, 2)] += 2.0 * prob / 36

            adj[pack(ind, 1)][pack(sq, 0)] += 1.0 * prob / 36         # case double roll
            adj[pack(ind, 2)][pack(sq, 1)] += 1.0 * prob / 36

        for ind, prob in next_ind_prob(sq, 5):
            adj[pack(ind, 0)][pack(sq, 0)] += 4.0 * prob / 36          
            adj[pack(ind, 0)][pack(sq, 1)] += 4.0 * prob / 36
            adj[pack(ind, 0)][pack(sq, 2)] += 4.0 * prob / 36

        for ind, prob in next_ind_prob(sq, 6):
            adj[pack(ind, 0)][pack(sq, 0)] += 4.0 * prob / 36         
            adj[pack(ind, 0)][pack(sq, 1)] += 4.0 * prob / 36
            adj[pack(ind, 0)][pack(sq, 2)] += 4.0 * prob / 36

            adj[pack(ind, 1)][pack(sq, 0)] += 1.0 * prob / 36          
            adj[pack(ind, 2)][pack(sq, 1)] += 1.0 * prob / 36

        for ind, prob in next_ind_prob(sq, 7):
            adj[pack(ind, 0)][pack(sq, 0)] += 6.0 * prob / 36         
            adj[pack(ind, 0)][pack(sq, 1)] += 6.0 * prob / 36
            adj[pack(ind, 0)][pack(sq, 2)] += 6.0 * prob / 36

        for ind, prob in next_ind_prob(sq, 8):
            adj[pack(ind, 0)][pack(sq, 0)] += 4.0 * prob / 36         
            adj[pack(ind, 0)][pack(sq, 1)] += 4.0 * prob / 36
            adj[pack(ind, 0)][pack(sq, 2)] += 4.0 * prob / 36

            adj[pack(ind, 1)][pack(sq, 0)] += 1.0 * prob / 36          
            adj[pack(ind, 2)][pack(sq, 1)] += 1.0 * prob / 36

        for ind, prob in next_ind_prob(sq, 9):
            adj[pack(ind, 0)][pack(sq, 0)] += 4.0 * prob / 36          
            adj[pack(ind, 0)][pack(sq, 1)] += 4.0 * prob / 36
            adj[pack(ind, 0)][pack(sq, 2)] += 4.0 * prob / 36
        
        for ind, prob in next_ind_prob(sq, 10):
            adj[pack(ind, 0)][pack(sq, 0)] += 2.0 * prob / 36          
            adj[pack(ind, 0)][pack(sq, 1)] += 2.0 * prob / 36
            adj[pack(ind, 0)][pack(sq, 2)] += 2.0 * prob / 36

            adj[pack(ind, 1)][pack(sq, 0)] += 1.0 * prob / 36         
            adj[pack(ind, 2)][pack(sq, 1)] += 1.0 * prob / 36

        for ind, prob in next_ind_prob(sq, 11):
            adj[pack(ind, 0)][pack(sq, 0)] += 2.0 * prob / 36         
            adj[pack(ind, 0)][pack(sq, 1)] += 2.0 * prob / 36
            adj[pack(ind, 0)][pack(sq, 2)] += 2.0 * prob / 36

        for ind, prob in next_ind_prob(sq, 12):
            adj[pack(ind, 1)][pack(sq, 0)] += 1.0 * prob / 36         
            adj[pack(ind, 2)][pack(sq, 1)] += 1.0 * prob / 36        
        
        adj[pack(c2J, 0)][pack(sq, 2)] += 6.0 / 36   

def markov_builder_2_die4f():
    for sq in range(40):
        for ind, prob in next_ind_prob(sq, 2):
            adj[pack(ind, 1)][pack(sq, 0)] += 1.0 * prob / 16        # rolls double 1, no double so far
            adj[pack(ind, 2)][pack(sq, 1)] += 1.0 * prob / 16        # rolls double 1, one double so far

        for ind, prob in next_ind_prob(sq, 3):
            adj[pack(ind, 0)][pack(sq, 0)] += 2.0 * prob / 16         
            adj[pack(ind, 0)][pack(sq, 1)] += 2.0 * prob / 16
            adj[pack(ind, 0)][pack(sq, 2)] += 2.0 * prob / 16
        
        for ind, prob in next_ind_prob(sq, 4):
            adj[pack(ind, 0)][pack(sq, 0)] += 2.0 * prob / 16         # case for non double roll
            adj[pack(ind, 0)][pack(sq, 1)] += 2.0 * prob / 16
            adj[pack(ind, 0)][pack(sq, 2)] += 2.0 * prob / 16

            adj[pack(ind, 1)][pack(sq, 0)] += 1.0 * prob / 16         # case double roll
            adj[pack(ind, 2)][pack(sq, 1)] += 1.0 * prob / 16

        for ind, prob in next_ind_prob(sq, 5):
            adj[pack(ind, 0)][pack(sq, 0)] += 4.0 * prob / 16          
            adj[pack(ind, 0)][pack(sq, 1)] += 4.0 * prob / 16
            adj[pack(ind, 0)][pack(sq, 2)] += 4.0 * prob / 16

        for ind, prob in next_ind_prob(sq, 6):
            adj[pack(ind, 0)][pack(sq, 0)] += 2.0 * prob / 16        
            adj[pack(ind, 0)][pack(sq, 1)] += 2.0 * prob / 16
            adj[pack(ind, 0)][pack(sq, 2)] += 2.0 * prob / 16

            adj[pack(ind, 1)][pack(sq, 0)] += 1.0 * prob / 16         
            adj[pack(ind, 2)][pack(sq, 1)] += 1.0 * prob / 16

        for ind, prob in next_ind_prob(sq, 7):
            adj[pack(ind, 0)][pack(sq, 0)] += 2.0 * prob / 16         
            adj[pack(ind, 0)][pack(sq, 1)] += 2.0 * prob / 16
            adj[pack(ind, 0)][pack(sq, 2)] += 2.0 * prob / 16

        for ind, prob in next_ind_prob(sq, 8):
            adj[pack(ind, 1)][pack(sq, 0)] += 1.0 * prob / 16         
            adj[pack(ind, 2)][pack(sq, 1)] += 1.0 * prob / 16        

        adj[pack(c2J, 0)][pack(sq, 2)] += 4.0 / 16   

markov_builder_2_die4f()

for i in range(100):
    vprob = [sum(adj[j][k] * vprob[k] for k in range(120)) for j in range(120)]

ans = [(str(x) if x > 9 else '0' + str(x), vprob[pack(x,0)] + vprob[pack(x,1)] + vprob[pack(x,2)]) for x in range(40)]
ans = sorted(ans, key=lambda x: x[1], reverse=True)
print('The six digit modal string is: {0}'.format(ans[0][0] + ans[1][0] + ans[2][0]))