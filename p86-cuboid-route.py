'''
An integer shortest path N on the cuboid a x b x c corresponds to a right triangle a^2 + (b + c)^2 = N^2.
Hence, we use Euler's formula to generate the legs m^2-n^2 and 2*m*n. Denote bc = b + c.  
The maximal m we look for is given by m^2 - n^2 < m^2 <= 2*M, where bc <= 2*M. Suppose we fix a = m^2-n^2, then,
we count the number of partitions of bc = 2*m*n into parts b and c such that the cuboid a x b x c is unique. 
We also need to satisfy the property (a + b)^2 + c^2 >= a^2 + (b + c)^2, otherwise, the shortest length N 
is not sqrt(a^2 + (b + c)^2) but is instead sqrt((a + b)^2 + c^2). This gives us two cases: if bc < a, 
then, (a + b)^2 + c^2 > a^2 + (b + c)^2 will always be true. Hence, the number of distinct partitions
are floor(bc / 2) due to symmetry. If bc > a, then both b <= a and c <= a is required for valid cases. If c > a, 
then, (a + b)^2 + c^2 < a^2 + (b + c)^2 which is not valid. Assume b >= c, then the minimum b = ceil(bc / 2), and
the range of allowed partitions are a - ceil(bc / 2) + 1. If a < ceil(bc / 2), there are no possible partitions,
therefore, the expression above would evaluate as max(0, a - ceil(bc / 2) + 1). The answer is found by 
incrementing M until the cuboid tally is above 1 million.
'''

import math

def ceil(a, b):
    return -(a // -b)

def find_cuboid_M():
    M = 100
    while True:
        memA, m = {}, 2, 
        cubs, M = 0, M + 1
        for m in range(int(math.sqrt(2*M)) + 1):
            for n in range(1, m):
                if math.gcd(m,n) == 1:
                    a, bc = m*m - n*n, 2*m*n
                    for a, bc in [(a, bc), (bc, a)]:
                        k = 1
                        while k * a <= M and k * bc <= 2*M:
                            ka, kbc = a * k, bc * k
                            if ka not in memA:
                                memA[ka] = []
                            if memA[ka].count(kbc) == 0:
                                memA[ka].append(kbc)
                                cubs += kbc // 2 if kbc < ka else max(0, ka - ceil(kbc, 2) + 1)

                            k += 1
                            if cubs > int(1e6):
                                return M
        
print('The minimal M that contains more than 1 million distinct \
cuboids with integer shortest paths is: {0}'.format(find_cuboid_M()))