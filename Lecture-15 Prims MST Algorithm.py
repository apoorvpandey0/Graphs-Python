# This is the lazy implementation of Prim's Algorithm
from heapq import *
# Node format [cost,nodeTo]
g = {
    0: [[10,1], [1,2], [4,3]],
    1: [[10,0], [0,4], [3,2]],
    2: [[1,0], [2,3], [8,5], [3,1]],
    3: [[4,0], [2,2], [2,5], [7,6]],
    4: [[0,1], [1,5], [8,7]],
    5: [[1,4], [9,7], [6,6], [2,3], [8,2]],
    6: [[12,7], [6,5], [7,3], [6,5]],
    7: [[12,6], [9,5], [8,4]]
}

pq = []
heapify(pq)

N = len(g)

visited = [False for i in range(N)]

def addEdges(nodeIndex):
    # print("Adding neighbours of:",nodeIndex)
    # Mark the current node as visited
    visited[nodeIndex] = True

    # Iterate over all edges going outwards from the current node
    # Add edges to pq which point to unvisited nodes
    edges = g[nodeIndex]
    for edge in edges:
        if not visited[edge[1]]:
            heappush(pq,edge)
    # print("PQ:",pq)
def lazyPrims(g,s):
    m = N-1     # Number of edges in MST = No of vertices - 1
    edgeCount,mstCost = 0,0
    mstEdges = [None for i in range(m)]
    addEdges(s)

    while len(pq) and edgeCount != m:
        edge = heappop(pq)
        nodeIndex = edge[1]

        if visited[nodeIndex]: continue

        mstEdges[edgeCount] = edge
        edgeCount+=1
        mstCost += edge[0]

        addEdges(nodeIndex)

    if edgeCount !=m :
        # i.e. no MST exists 
        return (None,None)
        
    return (mstCost, mstEdges)

print(lazyPrims(g,0))