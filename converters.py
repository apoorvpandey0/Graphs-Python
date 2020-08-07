from sys import maxsize
p = {
    0:[[1,5]],
    1:[[2,20],[5,30],[6,60]],
    2:[[3,10],[4,75]],
    3:[[2,-15]],
    4:[[9,100]],
    5:[[6,5],[8,50],[4,25]],
    6:[[7,-50]],
    7:[[8,-10]],
    8:[],
    9:[]
}

def listToMatrix(lst):
    """For weighted Adjacency list -> weighted Matrix conversion"""
    N = len(lst)
    M = [[0 for i in range(N)] for j in range(N)]

    for row in lst:
        for col in lst[row]:
            node,edge = col[0],col[1]
            M[row][node] = edge
    return M

def matrixToList(M):
    """For weighted Matrix -> weighted Adjacency list conversion"""
    N = len(M)
    lst = { row:[] for row in range(N) }
    for row in range(N):
        for col in range(N):
            if M[row][col]:
                lst[row].append([col,M[row][col]])
    print(lst)
    return lst

def listToEdge(lst):
    """For weighted adjacency lists -> weighted edge list conversion"""
    edges = []
    for vertex in lst:
        for edge in lst[vertex]:
            edges.append([vertex]+edge)
    return edges

if __name__=='__main__':
    # 1
    # a = listToMatrix(p)
    # print(p)
    # for i in a:
        # print(i)
    
    # 2
    # matrixToList(a)    

    # 3
    # print(listToEdge(p))
    print("Hello World")