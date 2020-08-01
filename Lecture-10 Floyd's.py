from sys import maxsize
p = {  0:[1,9],
       1:[0,8],
       2:[3,8],
       3:[2,4,5],
       4:[3],
       5:[3,6],
       6:[5,7],
       7:[8,11,10,6],
       8:[7,1,9,2],
       9:[0,8,10],
       10:[7,11,9],
       11:[7,10],
       12:[]}
# g = {1: [2, 3], 2: [1], 3: [1], 4: []}
g = {1: [], 2: [
    
    
    
    
    
    
    
    
    
    
    
    3], 3: [2]}
def bfs():
    N = len(g)
    V = [False for i in range(N+1)]
    D = [maxsize for i in range(N+1)]
    s = 2
    q = [s]
    D[s] = 0
    while len(q):
        node = q[0]
        V[q[0]] = True
        # print("For node {}".format(node))
        neighbours = g[node]
        for ele in neighbours:
            if not V[ele] :
                q.append(ele)
                V[ele] = True
                if D[node] + 6 < D[ele]:
                    D[ele] = D[node] + 6 
        q = q[1:]
    for i in range(len(D)):
        if D[i] == maxsize:
            D[i] = -1
    D.pop(s)
    print(D[1:])
bfs()