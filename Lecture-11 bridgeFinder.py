# Bridge finding algorithm
g = {  0:[1,9],
       1:[0,8],
       2:[3],
       3:[2,7,4,5],
       4:[3],
       5:[3,6],
       6:[5,7],
       7:[8,10,6,3],
       8:[1,9,7],
       9:[0,8],
       10:[7,11],
       11:[10]
}

id = 0  # The always incrementing counter 
N = len(g)

ids = [0 for i in range(N)]
visited = [False for i in range(N)]
low = [0 for i in range(N)]
bridges = []

order = []

def dfs(at,parent):
    # print("Started DFS at {} from {}".format(at,parent))
    global id
    visited[at] = True
    ids[at] = low[at] = id      # To assign node id as initial low values
    id += 1

    order.append(at)
    # Looping over neighbours of 'at'
    # print("    Neighbours of {} are {}".format(at,g[at]))
    for to in g[at]:
        if to == parent : continue
        if not visited[to]:
            # print("        Started DFS at {} from {}".format(to,at))
            dfs(to,at)
            # print("Updating low[{}] by {}".format(at,min(low[at],low[to])))
            low[at] = min(low[at],low[to])
            
            # print("ID:",ids)
            # print("LOW:",low)
            
            if ids[at] < low[to] :
                bridges.append((at,to))
                # bridges.append(to)

        else:
            # print("Else Updating low[{}] by {}".format(at,min(low[at],low[to])))
            low[at] = min(low[at],ids[to])



def bridgeFinder():
    # To loop over each connected component
    # Since one dfs run will cover an entire connected component 
    for i in g:
        if not visited[i]:
            dfs(i,-1)
    print(bridges)
    # print(low)
    # print(ids)
    # print(order)

bridgeFinder()