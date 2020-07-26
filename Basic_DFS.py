# This is basic DFS algorithm implementation with adjacency list
# The worst case time complexity of the algorithm is O(V+E)
# i.e sum of number of vertices and edges

g = {  0:[1,9],
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
       11:[7,10]}
visited = [ False for i in g]
calls = 0
def dfs(at):
    global calls
    calls += 1
    # print(visited)
    if visited[at] : return
    visited[at] = True
    neighbours = g[at]
    for next in neighbours:
        dfs(next)

dfs(0)
print('Time complexity part:')
print("Number of calls to dfs fn:",calls)
edges = 0
for i in g:
    edges+=len(g[i])
print("Sum of number of vertices and edges:",len(g)+edges)