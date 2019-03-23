import msvcrt
from os import system, name


class Player:
    def __init__(self, x, y):
        self.xPos = x
        self.yPos = y
        self.xLastPos = x
        self.yLastPos = y

    def printPos(self):
        print("Player is in (", self.xPos, ", ", self.yPos, ")")

    # getters
    def getCellPos(self):
        pos = {}
        pos["x"] = self.xPos
        pos["y"] = self.yPos
        return pos

    def getXPos(self):
        return self.xPos

    def getYPos(self):
        return self.yPos

    def getXLastPos(self):
        return self.xLastPos

    def getYLastPos(self):
        return self.yLastPos

    # setters
    def setPos(self, x, y):
        self.xPos = x
        self.yPos = y

    def moveUp(self):
        self.yLastPos = self.yPos
        self.yPos = self.yPos-1

    def moveDown(self):
        self.yLastPos = self.yPos
        self.yPos = self.yPos+1

    def moveLeft(self):
        self.xLastPos = self.xPos
        self.xPos = self.xPos-1

    def moveRight(self):
        self.xLastPos = self.xPos
        self.xPos = self.xPos+1


class Maze:
    representation = {0: ' ', 1: 'x', 5: 'E', 10: 'C', 2: 'P'}

    def __init__(self):
        self.maze = []
        self.visitedCells = []
        self.pathTakenCells = []
        self.rowList0 = []
        self.rowList1 = []
        self.rowList2 = []
        self.rowList3 = []
        self.rowList4 = []
        self.rowList5 = []
        self.rowList6 = []
        self.rowList7 = []
        self.rowList8 = []
        self.rowList9 = []
        self.createMaze()

    def createMaze(self):
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
        self.maze = [self.rowList0, self.rowList1, self.rowList2, self.rowList3, self.rowList4,
                     self.rowList5, self.rowList6, self.rowList7, self.rowList8, self.rowList9]

    def printMaze(self, p):
        self.createMaze()
        entrance = False
        if (p.getXPos() == 1) and (p.getYPos() == 0):
            # Player is standing at entrance
            entrance = True
        self.maze[p.getYPos()][p.getXPos()] = 2
        # Draw maze
        for m in self.maze:
            for c in m:
                print("  {}  ".format(self.representation[c]), end="")
            print()
        # End draw maze
        if (entrance):
            self.maze[p.getYPos()][p.getXPos()] = 5

    def gameOver(self, p):
        if self.maze[p.yPos][p.xPos] == 10:
            # Player is standing at exit
            ok = 1
        else:
            ok = 0
        return ok

    def addVisitedCell(self, x, y):
        cell = {}
        cell["x"] = x
        cell["y"] = y
        self.visitedCells.append(cell)

    def addPathTakenCell(self, x, y):
        cell = {}
        cell["x"] = x
        cell["y"] = y
        self.pathTakenCells.append(cell)

    def popVisitedCell(self):
        return self.visitedCells.pop()

    def isVisitedCell(self, x, y):
        isVisited = False
        for c in self.visitedCells:
            if ((c["x"] == x) and (c["y"] == y)):
                isVisited = True
        return isVisited


class Game:
    def __init__(self):
        self.m = Maze()
        self.p = Player(1, 0)
        self.m.printMaze(self.p)
        self.limit = 10

    def canMove(self, direction):
        # direction values: 1 is up, 2 is right, 3 is down, 4 is left
        mov = False
        if (direction == 1):
            # trying to move UP
            if (self.p.getYPos()-1 >= 0) and (self.m.maze[self.p.getYPos()-1][self.p.getXPos()] != 1):
                mov = True
        if (direction == 3):
            # trying to move DOWN
            if (self.p.getYPos()+1 < self.limit) and (self.m.maze[self.p.getYPos()+1][self.p.getXPos()] != 1):
                mov = True
        if (direction == 2):
            # trying to move RIGHT
            if (self.p.getXPos()+1 <= self.limit) and (self.m.maze[self.p.getYPos()][self.p.getXPos()+1] != 1):
                mov = True
        if (direction == 4):
            # trying to move LEFT
            if (self.p.getXPos()-1 > 0) and (self.m.maze[self.p.getYPos()][self.p.getXPos()-1] != 1):
                mov = True
        return mov

    def canMoveIA(self):
        # direction values: 1 is up, 2 is right, 3 is down, 4 is left
        mov = 0
        if (self.p.getYPos()-1 >= 0) and (self.m.maze[self.p.getYPos()-1][self.p.getXPos()] != 1) and (self.m.isVisitedCell(self.p.getXPos(), self.p.getYPos()-1) == 0):
            mov = 1
        if (self.p.getYPos()+1 < self.limit) and (self.m.maze[self.p.getYPos()+1][self.p.getXPos()] != 1) and (self.m.isVisitedCell(self.p.getXPos(), self.p.getYPos()+1) == 0):
            mov = 3
        if (self.p.getXPos()+1 <= self.limit) and (self.m.maze[self.p.getYPos()][self.p.getXPos()+1] != 1) and (self.m.isVisitedCell(self.p.getXPos()+1, self.p.getYPos()) == 0):
            mov = 2
        if (self.p.getXPos()-1 > 0) and (self.m.maze[self.p.getYPos()][self.p.getXPos()-1] != 1) and (self.m.isVisitedCell(self.p.getXPos()-1, self.p.getYPos()) == 0):
            mov = 4
        return mov

    def manualPlay(self):
        win = 0
        while (win == 0):
            if msvcrt.kbhit():
                # key = msvcrt.getch()
                kp = str(msvcrt.getch()).replace("b'", "").replace("'", "")
                system('cls')
                if kp == 'M':
                    if (self.canMove(2)):
                        self.p.moveRight()
                        if(self.m.gameOver(self.p)):
                            win = 1
                            system('cls')
                            print("YOU WIN!")
                if kp == 'K':
                    if (self.canMove(4)):
                        self.p.moveLeft()
                if kp == 'H':
                    if (self.canMove(1)):
                        self.p.moveUp()
                if kp == 'P':
                    if (self.canMove(3)):
                        self.p.moveDown()
                self.m.printMaze(self.p)

    def autoPlay(self):
        win = 0
        while (win == 0):
            direction = self.canMoveIA()
            system('cls')
            while (direction != 0):
                if (direction == 1):
                    self.p.moveUp()
                if (direction == 2):
                    self.p.moveRight()
                    if(self.m.gameOver(self.p)):
                        win = 1
                        system('cls')
                        print("YOU WIN!")
                if (direction == 3):
                    self.p.moveDown()
                if (direction == 4):
                    self.p.moveLeft()
                self.m.printMaze(self.p)
                direction = self.canMoveIA()
                t=input()
                print(direction)
            
            print("Nos la pusimos")
            t=input()

print("Press ENTER to start")
t = input()

g = Game()

# Select True or False to play manual or automatic
if (False):
    g.manualPlay()
else:
    g.autoPlay()

print("Game finished. Thank you for playing!")
