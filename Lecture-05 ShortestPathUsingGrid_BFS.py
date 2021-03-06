# Using BFS to find out the shortest path in a 2D Grid
# Here: 0 represents an empty cell
    #   1 represents a rock
    #   2 represents an exit
# TODO:   1.Implement a Prev Matrix to track the exact path
from collections import deque 

# Global/class scope variables
M = [
    [0,0,0,1,0,0,0],
    [0,1,0,0,0,1,0],
    [0,1,0,0,0,0,0],
    [0,0,1,1,0,0,0],
    [1,0,1,2,0,1,0]
]
# Path = [0,0] -> [0,1] -> [0,2] -> [1,2] -> 

R,C = len(M), len(M[0]) #Size of the matris M
sr=sc=0 #coordinates of starting node

prev = [ [None for i in range(C)] for j in range(R)]
# print(prev)

#Do not do rq = zq = dequeue() , they both will have the same memory wrna
rq = deque() #Empty queue for tracking row values
cq = deque() #Empty queue for tracking column values

reached_end = False
visited = [[False for i in range(C)] for i in range(R) ]

#Vaiables used to track the number of steps taken
move_count = 0
nodes_left_in_layer = 1
nodes_in_next_layer = 0

# Direction vectors of North,South,East,West
dr = [-1,1,0,0]
dc = [0,0,+1,-1]

# prev = [[None for i in range(R)] for j in range(N)]
def explore(r,c):
    global nodes_in_next_layer
    global prev
    # print("Exploring:",(r,c))
    for i in range(len(dr)):   #For each direction
        nr = r + dr[i]         #New row = initial row + dr
        nc = c + dc[i]         #New col = initial col + dc
    
        #Boundaries check
        if nr<0 or nc<0: continue
        if nr>=R or nc>=C: continue

        #Skip the visited nodes
        if visited[nr][nc]: continue
        if M[nr][nc] == 1: continue
        # print(nr,nc)

        rq.append(nr)
        cq.append(nc)
        prev[nr][nc] = [r,c]
        # print("position:",(nr,nc),"element:",M[nr][nc])
        # print("Updated queue with:",(nr,nc))

        visited[nr][nc] = True
        nodes_in_next_layer+=1

def solve():
    global nodes_left_in_layer
    global nodes_in_next_layer
    global move_count
    global reached_end
    rq.append(sr)
    cq.append(sc)
    # print("Added first values to rq and cq:",rq,cq)
    visited[sr][sc] = True
    while len(rq):
        # print("Queue stats:",list(zip(rq,cq)),end='\n')
        r = rq.popleft()
        c = cq.popleft()
        # print("Popped out left element:",r,c)
        if M[r][c] == 2:
            reached_end = True 
            break
        explore(r,c)
        # print("Queue stats:",list(zip(rq,cq)))
        # print("Nodes left",nodes_left_in_layer)
        # print("Nodes next",nodes_in_next_layer)
        nodes_left_in_layer-=1
        if nodes_left_in_layer == 0:
            # print("Layer",list(zip(rq,cq)))
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count+=1
    if reached_end:
        return move_count
    return -1
def router(prev,s=[],e=[]):
    node = e
    path = [node]
    while node != s:
        node = prev[node[0]][node[1]]
        path.append(node)
    return path

print("Steps required to reach the end:",solve())
print("Path is:",router(prev,[0,0],[4,3]))
