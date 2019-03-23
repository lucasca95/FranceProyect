
def createMaze(fil, col, n):
    N=n
    while N>0:
        col.append("x")
        N=N-1
    N=n
    while N>0:
        fil.append(col)
        N=N-1
    return fil

def printMaze(maze):
    for f in maze:
        print(f)

def createRoad(maze):
    maze[0][1]=" "
    return maze

col=[]
maze=[]
N=10
#maze=createMaze(maze, col, N)
#maze=createRoad(maze)
#printMaze(maze)