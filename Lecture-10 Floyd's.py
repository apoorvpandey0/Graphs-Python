# This is still under construction

from sys import maxsize
N = 4   #Size of adjacency matrix
dp = [[maxsize for i in range(N)] for j in range(N)]    # The memo table that will contain APSP soln
agla = [[None for i in range(N)] for j in range(N)]     # Matrix used to reconstruct the shortest path

def setup(m):
    # dp = [[maxsize for i in range(N)] for j in range(N)]
    # agla = [[None for i in range(N)] for j in range(N)]

    for i in range(N):
        for j in range(N):
            dp[i][j] = m[i][j]
            if m[i][j] != maxsize :
                agla[i][j] = j

def propogateNegativeCycles(dp,N):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dp[i][k] + dp[k][j] < dp[i][j] :
                    dp[i][j] = maxsize*-1
                    agla[i][j] = -1

def reconstructPath(start,end):
    path = []
    # Check if there exista a path b/w the start and end node
    if dp[start][end] == maxsize: return path

    at = start
    # Reconstruct the path from agla matrix
    while at!=end :
        if at == -1 : return None
        path.append(at)
        at = agla[at][end]

def floydWarshall(m):
    setup(m)

    # Execute FWSPA
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dp[i][k] + dp[k][j] < dp[i][j] :
                    dp[i][j] = dp[i][k] + dp[k][j]
                    agla[i][j] = agla[i][k]
    
    # Detect and propogate Negative cycles
    # propogateNegativeCycles(dp,N)

    # Return APSP matrix
    return dp
m =[ 
    [0, 5, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 20, 0, 0, 30, 60, 0, 0, 0],
    [0, 0, 0, 10, 75, 0, 0, 0, 0, 0],
    [0, 0, -15, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 100],
    [0, 0, 0, 0, 25, 0, 5, 0, 50, 0],
    [0, 0, 0, 0, 0, 0, 0, -50, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, -10, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
print(floydWarshall(m))
