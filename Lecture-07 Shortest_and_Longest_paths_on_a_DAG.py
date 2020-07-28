# This algorithm finds the sortest path between two nodes in a directed acyclic and weighted graph
# The weights can be positive,negative or zero it dosent matters
# Time complexity is O(V+E)
from sys import maxsize
g = {
    0:[ [1,3], [2,6] ],
    1:[ [2,4], [3,4], [4,11] ],
    2:[ [3,8], [6,11] ],
    3:[ [4,-4],[5,5], [6,2] ],
    4:[ [7,9] ],
    5:[ [7,1] ],
    6:[ [7,2] ],
    7:[]
}

N = len(g)
V = [False for i in range(N)]
def dfs(at,visitedNodes):
    V[at] = True
    # print("Neighbours of {} are {}".format(at,g[at]))
    for next in g[at]: 
        if V[next[0]] == False:
            # print("Visited:",V)
            dfs(next[0],visitedNodes)
    # print('Visited nodes list:',visitedNodes)
    visitedNodes.append(at)
def topSort():
    ordering = [0 for i in range(N)]
    i = N-1  #Index for ordering array

    for at in range(N):  #For each node in the graph run DFS on it if unvisited
        # print("Calling DFS for:",at)
        if V[at] == False:
            visitedNodes = []
            dfs(at,visitedNodes)
            for nodeId in visitedNodes:
                ordering[i] = nodeId
                i -= 1
            # print(ordering)
    return ordering
# print(topSort())
def shortestPath(g,frm):
    N = len(g)  
    # visited = [False for i in range(N)]
    ordering = topSort()
    print("Topological ordering:",ordering)

    DTable = [maxsize for i in range(N)]    # To maintain the distances from starting node to all others
    DTable[frm] = 0
    
    for node in ordering:
        print("Selected Node from ordering:",node)
        neighbours = g[node]
        # print(" Neighbours of node {} are {}:".format(node,g[node]))
        for next in neighbours:
            next_key,next_value = next
            # print("     Checking for neigbhour ({},{})".format(next_key,next_value))
            if next_value + DTable[node] < DTable[next_key]:
                # print("         Updating DTable{} with {}".format(next_key,DTable[node] + next_value))
                DTable[next_key] = DTable[node] + next_value
    return DTable
from_node = 1
# print("The shortest distances from node {} to all other nodes are:".format(from_node),shortestPath(g,from_node))

def longestPath(g):
    # First we need to negate all the edge values
    for node in g:
        neighbours = g[node]
        for next in neighbours:
            next[1]*=-1
    # Now we need to run our shortestPath algorithms
    print(shortestPath(g,0))
    # Again negate the distanes returned by shortestPath to get the longest path !
longestPath(g)



