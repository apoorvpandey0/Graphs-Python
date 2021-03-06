# Tarjans algorithm to find strongly connected components
# Strongly connected components are self contained cycles in a directed graph

g = {
    0:[1,2],
    1:[0,3],
    2:[3],
    3:[4,5],
    4:[2,5,6],
    5:[7],
    6:[5],
    7:[6]
}
N = len(g)
UNVISITED = -1
id = 0
sccCount = 0

ids = [0 for i in range(N)]
low = [0 for i in range(N)]
onStack = [0 for i in range(N)]
stack = []

def dfs(at):
    # print("Started DFS at:",at)
    global sccCount
    global id

    stack.append(at)
    onStack[at] = True
    ids[at] = low[at] = id
    id+=1

    # Visit the neighbours and min low-link on callback
    for to in g[at]:
        if ids[to] == UNVISITED : dfs(to)
        if onStack[to]: low[at] = min(low[at],low[to])
    # print("IDS",ids)
    # After having visited all the neighbours of 'at'
    # if we're at the start node of a SCC then empty the 
    # seen stack until we're back on start node

    # print("ids:",ids)
    # print("lows:",low)
    
    if ids[at] == low[at]:
        while 1:
            node = stack.pop()
            # print("     popped:",node,at)
            onStack[node] = False
            if node == at: break
        sccCount+=1
    # print("SCCCount",sccCount)
    # print(stack)
def sccTarjans(g):
    for i in range(N): ids[i] = UNVISITED   # Unhi
    for i in range(N):
        if ids[i] == UNVISITED:
            dfs(i)
    return low

# print(sccTarjans({1:[2],2:[1,5],3:[4],4:[3,5],5:[6],6:[7],7:[8],8:[6,9],9:[]}))
print("KEY wise:",sccTarjans(g))
print("SCCCount",sccCount)