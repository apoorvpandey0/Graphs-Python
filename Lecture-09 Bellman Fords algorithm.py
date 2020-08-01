# This is an implementation of Bellman Fords algorithm
# Time complexity O(EV) or O((E+V)*log(V))
# This is a SSSP algorithm which works on Directed graphs with weighted edges
# This algorithm is used for detecting negative cycles in the graph and marking them out

# The following implementation has a bad time complexity O(n^3)
# A better approach would be to get all the edges first in a list and then loop over
from sys import maxsize
import pdb

p = {
    0:[ [1,3], [2,6] ],
    1:[ [2,4], [3,4], [4,11] ],
    2:[ [3,8], [6,11] ],
    3:[ [4,-4],[5,5], [6,2] ],
    4:[ [7,9] , [4,-10]],
    5:[ [7,1] ],
    6:[ [7,2] ],
    7:[]
}
g = {
    0:[[1,5]],
    1:[[2,20],[5,30],[6,60]],
    2:[[3,10],[4,75]],
    3:[[2,-15]],
    4:[[9,100]],
    5:[[6,5],[8,50],[4,25]],
    6:[[7,-50]],
    7:[[8,-10]],
    8:[],
    9:[]
}
def bfalgo():
    N = len(g)
    D = [maxsize for i in range(N)]
    D[0] = 0
    for _ in range(N-1):
        for i in range(N-1):
            # print("For node {}".format(i))
            for node in g[i]:
                # print(" Checking neighbour {}".format(node))
                # print(D)
                if D[i] + node[1] < D[node[0]] :
                    # pdb.set_trace()
                    # print("     Updating {} with {} + {}".format(D[node[0]],D[i],node[1]))
                    D[node[0]] =  D[i] + node[1]
    print(D)
    for i in range(N-1):
        # print("For node {}".format(i))
        for node in g[i]:
            # print(" Checking neighbour {}".format(node))
            if D[i] + node[1] < D[node[0]] :
                # print("    Updating {}".format(node[0]))
                D[node[0]] =  maxsize*-1
            # print(D)
    print(D)    

bfalgo()