a=[
	[1,1,1,0,0,1,1],
	[1,0,1,0,0,0,0],
	[1,0,1,0,0,1,0],
	[1,1,1,0,0,0,1]
]
print(a)
rows = len(a)
cols = len(a[0])
islands = 0

def traverse(x,y):
	if x<0 or y<0 or x>rows-1 or y>cols-1 :
		#Boundary Conditions
		return

	a[x][y] = 2 #i.e. we have visited the element

	if x<rows-1 and a[x+1][y]==1 : #Down
		traverse(x+1,y)
	if y<cols-1 and a[x][y+1]==1: #Right
		traverse(x,y+1)
	if a[x-1][y]==1: #Up
		traverse(x-1,y)
	if a[x][y-1]==1: #Left
		traverse(x,y-1)
	return

for i in range(rows):
	for j in range(cols):
		if a[i][j]==1:
			islands+=1
			traverse(i,j)
print(a)
print(islands)
