# Using BFS to find out the shortest path in a 2D Grid
# Here: 0 represents an empty cell
    #   1 represents a rock
    #   2 represents an exit

from collections import deque 

# Global/class scope variables
M = [
    [0,0,0,1,0,0,0],
    [0,1,0,0,0,1,0],
    [0,1,0,0,0,0,0],
    [0,0,1,1,0,0,0],
    [1,0,1,2,0,1,0]
]
R,C = len(M), len(M[0]) #Size of the matris M
sr=sc=0 #coordinates of starting node
rq = deque()
cq = deque() #Empty queues for tracking rows and columns
reached_end = False
visited = [[False for i in range(C)] for i in range(R) ]

#Vaiables used to track the number of steps taken
move_count = 0
nodes_left_in_layer = 1
nodes_in_next_layer = 0

# Direction vectors of North,South,East,West
dr = [-1,1,0,0]
dc = [0,0,+1,-1]

def explore(r,c):
    global nodes_in_next_layer
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
        # print(rq,cq)
        r = rq.popleft()
        c = cq.popleft()
        # print("Popped out left element:",r,c)
        if M[r][c] == 2:
            reached_end = True 
            break
        explore(r,c)
        nodes_left_in_layer-=1
        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count+=1
    if reached_end:
        return move_count
    return -1
      
print("Steps required to reach the end:",solve())
