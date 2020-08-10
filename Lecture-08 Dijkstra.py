# Dijkstra's Algorithm
# Time Complexity of Dijkstra's Algorithm is O ( V 2 ) 
# but with min-priority queue it drops down to O ( V + E l o g V ) .

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

def dijkstra(g,frm):
    N = len(g)
    key,edge = 0,1
    visited = [False for i in range(N)]
    prev = [None for i in range(N)]
    dist = [maxsize for i in range(N)]
    dist[frm] = 0
    pq = []
    pq.append((frm,0))
    while not all(visited):
        # Sorting so that the most promising node is the first one
        pq.sort(key=lambda x:x[1])

        # Get the first node/ 'A' node in A->B
        index,minValue = pq[0]
        pq.pop(0)

        # Mark the node as visited
        visited[index] = True

        # if minimum distance to the node(index) is already found then skip the node
        if dist[index] < minValue: continue
        
        # print("On node {} and len(pq) is {}".format(index,len(pq)))
        # print(" Visited:",visited)
        # print(" PQ",pq)
        # print(" Distance",dist)

        # Iterate over all of its(index) neighbours
        for next in g[index]:
            if visited[next[key]]: continue
            # print("Checking Neghbour:{} of {}".format(next,index))
            newDist = dist[index] + next[edge]
            if newDist < dist[next[key]]:
                prev[next[key]] = index
                dist[next[key]] = newDist
                pq.append((next[key],newDist))
    router(prev,7)
    return dist,prev

def router(prev,end):
    at = end
    path = []
    while at!=None:
        path.append(prev[at])
        at = prev[at]
    # print("Shortest Path:",path)

print("dist,prev arrays:",dijkstra(g,0)[-1][-1])

