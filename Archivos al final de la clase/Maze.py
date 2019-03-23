
import msvcrt
import random
from os import system, name


def createMaze():
    rowList0 = [1, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    rowList1 = [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
    rowList2 = [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1]
    rowList3 = [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1]
    rowList4 = [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1]
    rowList5 = [1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1]
    rowList6 = [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1]
    rowList7 = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1]
    rowList8 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10]
    rowList9 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    maze = [rowList0, rowList1, rowList2, rowList3, rowList4,
            rowList5, rowList6, rowList7, rowList8, rowList9]
    return maze


def printMaze(maze, player):
    maze = createMaze()
    maze[player["yPos"]][player["xPos"]] = 2
    for m in maze:
        for c in m:
            if c == 5:
                print("E", end="")
            elif c == 10:
                print("C", end="")
            elif c == 2:
                print("P", end="")
            else:
                print(c, end="")
        print()


def printMazeInFile(maze):
    f = open("printedMaze.txt", "w")
    for m in maze:
        for c in m:
            if c == 5:
                f.write("E")
            elif c == 10:
                f.write("C")
            else:
                f.write(str(c))
        f.write("/n")
    f.close()


def moverDer(maze, player):
    if (maze[player["yPos"]][player["xPos"] + 1] != 1):
        player["xPos"] = player["xPos"]+1
        ok = 1
    else:
        ok = 0
    return ok


def moverIzq(maze, player):
    if maze[player["yPos"]][player["xPos"] - 1] == 0:
        player["xPos"] = player["xPos"]-1
        ok = 1
    else:
        ok = 0
    return ok


def moverArr(maze, player):
    if maze[player["yPos"]-1][player["xPos"]] == 0:
        player["yPos"] = player["yPos"]-1
        ok = 1
    else:
        ok = 0
    return ok


def moverAba(maze, player):
    if maze[player["yPos"]+1][player["xPos"]] == 0:
        player["yPos"] = player["yPos"]+1
        ok = 1
    else:
        ok = 0
    return ok


def posValida(maze, player):
    if maze[player["yPos"]][player["xPos"]] != 0:
        print("Se quiere acceder a zona prohibida")
        player["yPos"] = 0
        player["xPos"] = 1
        ok = 0
    else:
        ok = 1
    return ok

def gameOver(maze, player):
    if(maze[player["yPos"]][player["xPos"]] == 10):
        ok=1
    else:
        ok=0
    return ok


m = createMaze()


print(' ')
p={}
p["yPos"]=0
p["xPos"]=1

printMaze(m,p)

jugando = 1
while (jugando):

    if msvcrt.kbhit():
            # key = msvcrt.getch()
        kp = str(msvcrt.getch()).replace("b'", "").replace("'", "")
        print(kp)
        system('cls')
        if kp == 'M':
            if(moverDer(m,p)):
                print("SII mover Der")
                if(gameOver(m,p)):
                    printMaze(m,p)
                    jugando = 0
                    system('cls')
                    print("YOU WIN!")
                    print("YOU WIN!")
                    print("YOU WIN!")
                    print("YOU WIN!")
            else:
                print("NOO mover Der")
        if kp == 'K':
            if(moverIzq(m,p)):
                print("SII mover Izq")
            else:
                print("NOO mover Izq")
        if kp == 'H':
            if(moverArr(m,p)):
                print("SII mover Arr")
            else:
                print("NOO mover Arr")
        if kp == 'P':
            if(moverAba(m,p)):
                print("SII mover Aba")
            else:
                print("NOO mover Aba")
        printMaze(m,p)
