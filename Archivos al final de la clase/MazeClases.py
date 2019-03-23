import msvcrt
import random
from os import system, name
class Player:

    xPos = 1
    xPosAnt= 1
    yPos = 0
    yPosAnt = 0
    repAnt=5
    rep = 2
        

    def moveRight(self, m):
        if (m.maze[self.yPos][self.xPos + 1] != 1):
            self.xPosAnt=self.xPos
            self.yPosAnt=self.yPos
            self.repAnt=0
            self.xPos = self.xPos+1
            ok = 1
        else:
            ok = 0
        return ok

    def moveLeft(self, m):
        if m.maze[self.yPos][self.xPos - 1] == 0:
            self.xPosAnt=self.xPos
            self.yPosAnt=self.yPos
            self.repAnt=0
            self.xPos = self.xPos-1
            ok = 1
        else:
            ok = 0
        return ok

    def moveUp(self, m):
        if m.maze[self.yPos-1][self.xPos] == 0:
            self.xPosAnt=self.xPos
            self.yPosAnt=self.yPos
            self.repAnt=0
            self.yPos = self.yPos-1
            ok = 1
        else:
            ok = 0
        return ok

    def moveDown(self, m):
        if m.maze[self.yPos+1][self.xPos] == 0:
            self.xPosAnt=self.xPos
            self.yPosAnt=self.yPos
            self.repAnt=0
            self.yPos = self.yPos+1
            ok = 1
        else:
            ok = 0
        return ok


class Maze:
    
    

    representation = {0: ' ', 1: 'x', 5: 'E', 10: 'C', 2: 'P'}

    def __init__(self):
        self.maze=[]
        self.rowList0 = [1, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.rowList1 = [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
        self.rowList2 = [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1]
        self.rowList3 = [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1]
        self.rowList4 = [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1]
        self.rowList5 = [1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1]
        self.rowList6 = [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1]
        self.rowList7 = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1]
        self.rowList8 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10]
        self.rowList9 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.createMaze()

    def createMaze(self):
        self.maze = [self.rowList0, self.rowList1, self.rowList2, self.rowList3, self.rowList4,
                     self.rowList5, self.rowList6, self.rowList7, self.rowList8, self.rowList9]

    def printMaze(self, p):
        self.createMaze()
        self.maze[p.yPosAnt][p.xPosAnt]=p.repAnt
        self.maze[p.yPos][p.xPos] = 2
        for m in self.maze:
            for c in m:
                """if c == 5:
                    print(" E ", end="")
                elif c == 10:
                    print(" C ", end="")
                elif c == 2:
                    print(" P ", end="")
                else:"""
                print(" {} ".format(self.representation[c]), end="")
            print()

    def gameOver(self, p):
        if self.maze[p.yPos][p.xPos] == 10:
            ok = 1
        else:
            ok = 0
        return ok

m = Maze()

print(' ')
p = Player()

m.printMaze(p)

jugando = 1
while (jugando):

    if msvcrt.kbhit():
            # key = msvcrt.getch()
        kp = str(msvcrt.getch()).replace("b'", "").replace("'", "")
        print(kp)
        system('cls')
        if kp == 'M':
            if(p.moveRight(m)):
                print("SII mover Der")
                if(m.gameOver(p)):
                    m.printMaze(p)
                    jugando = 0
                    system('cls')
                    print("YOU WIN!")
                    print("YOU WIN!")
                    print("YOU WIN!")
                    print("YOU WIN!")
            else:
                print("NOO mover Der")
        if kp == 'K':
            if(p.moveLeft(m)):
                print("SII mover Izq")
            else:
                print("NOO mover Izq")
        if kp == 'H':
            if(p.moveUp(m)):
                print("SII mover Arr")
            else:
                print("NOO mover Arr")
        if kp == 'P':
            if(p.moveDown(m)):
                print("SII mover Aba")
            else:
                print("NOO mover Aba")
        m.printMaze(p)
