import msvcrt
import random
from os import system, name


class Player:

    xPos = 1
    xPosAnt = 1
    yPos = 0
    yPosAnt = 0
    repAnt = 5
    rep = 2

    def showPos(self):
        print("P esta en ( ", self.xPos, ", ", self.yPos, ")")


    def moveToPos(self, x, y):
        self.xPos = x
        self.yPos = y

    def moveRight(self):
        self.xPosAnt = self.xPos
        self.yPosAnt = self.yPos
        self.repAnt = 0
        self.xPos = self.xPos+1

    def moveLeft(self):
        self.xPosAnt = self.xPos
        self.yPosAnt = self.yPos
        self.repAnt = 0
        self.xPos = self.xPos-1

    def moveUp(self):
        self.xPosAnt = self.xPos
        self.yPosAnt = self.yPos
        self.repAnt = 0
        self.yPos = self.yPos-1

    def moveDown(self):
        self.xPosAnt = self.xPos
        self.yPosAnt = self.yPos
        self.repAnt = 0
        self.yPos = self.yPos+1


class Maze:

    representation = {0: ' ', 1: 'x', 5: 'E', 10: 'C', 2: 'P'}

    def __init__(self):
        self.maze = []
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

        self.celdasConocidas = []
        self.celdasVerdaderas = []

    def createMaze(self):
        self.maze = [self.rowList0, self.rowList1, self.rowList2, self.rowList3, self.rowList4,
                     self.rowList5, self.rowList6, self.rowList7, self.rowList8, self.rowList9]

    def printMaze(self, p):
        self.createMaze()
        self.maze[p.yPosAnt][p.xPosAnt] = p.repAnt
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
        p.showPos()

    def gameOver(self, p):
        if self.maze[p.yPos][p.xPos] == 10:
            ok = 1
        else:
            ok = 0
        return ok

    def addKnownCell(self, xv, yv):
        cell = {}
        cell["x"] = xv
        cell["y"] = yv
        self.celdasConocidas.append(cell)

    def addTrueCell(self, xv, yv):
        cell = {}
        cell["x"] = xv
        cell["y"] = yv
        self.celdasVerdaderas.append(cell)

    def esCeldaConocida(self, x, y):
        print(self.celdasConocidas)
        for c in self.celdasConocidas:
            if(c["y"] == y) and (c["x"] == x):
                print("La celda (", x, ", ", y, ") es conocida")
                t = input()
                return True
            else:
                print("La celda (", x, ", ", y, ") NO ES CONOCIDA")
                t = input()
        return False

    def esCeldaVerdadera(self, x, y):
        print("Se ejecuta esCeldaVerdadera")
        for c in self.celdasVerdaderas:
            if(c["y"] == y) and (c["x"] == x):
                print("La celda (", x, ", ", y, ") es verdadera")
                return True
            else:
                print("La celda (", x, ", ", y, ") NO ES VERDADERA")
            text = input()
        return False

    def popTrue(self):
        cell = self.celdasVerdaderas.pop()
        print("Se popea la celda ( ", cell["x"],
              ", ", cell["y"], ") de celdasVerdaderas")
        text = input()
        return cell

    def IAmove(self, x, y):
        cond1 = (self.maze[x][y-1] == 0)
        cond2 = (y-1 >= 0)
        cond3 = (self.esCeldaConocida(x, y-1) == False)
        print("Tengo camino a arriba? ", cond1)
        print("Tengo tablero a arriba? ", cond2)
        print("Arriba es celda nueva? ", cond3)
        t = input()
        m.printMaze(p)

        cond1 = (self.maze[x-1][y] == 0)
        cond2 = (x-1 >= 0)
        cond3 = (self.esCeldaConocida(x-1, y) == False)
        print("Tengo camino a la izq? ", cond1)
        print("Tengo tablero a la izq? ", cond2)
        print("Izq es celda nueva? ", cond3)
        t = input()
        m.printMaze(p)

        cond1 = (self.maze[x+1][y] == 0)
        cond2 = (x+1 < 10)
        cond3 = (self.esCeldaConocida(x+1, y) == False)
        print("Tengo camino a la der? ", cond1)
        print("Tengo tablero a la der? ", cond2)
        print("Der es celda nueva? ", cond3)
        t = input()
        m.printMaze(p)

        cond1 = (self.maze[x][y+1] == 0)
        cond2 = (y+1 < 10)
        cond3 = (self.esCeldaConocida(x, y+1) == False)
        print("Tengo camino abajo? ", cond1)
        print("Tengo tablero abajo? ", cond2)
        print("Abajo es celda nueva? ", cond3)
        t = input()
        m.printMaze(p)

        if ((self.maze[x][y-1] == 0) and (y-1 >= 0) and (self.esCeldaConocida(x, y-1) == False)):
            print("Entre en if de mover arriba, mov 1")
            print(" ")
            t = input()
            mov = 1
        elif ((self.maze[x][y+1] == 0) and (y+1 < 10) and (self.esCeldaConocida(x, y+1) == False)):
            print("Entre en if de mover abajo, mov 3")
            print(" ")
            t = input()
            mov = 3
        elif ((self.maze[x-1][y] == 0) and (x-1 >= 0) and (self.esCeldaConocida(x-1, y) == False)):
            print("Entre en if de mover izquierda, mov 4")
            print(" ")
            t = input()
            mov = 4
        elif ((self.maze[x+1][y] == 0) and (x+1 < 10) and (self.esCeldaConocida(x+1, y) == False)):
            print("Entre en if de mover derecha, mov 2")
            print(" ")
            t = input()
            mov = 2
        else:
            print("Entre en else, mov 0")
            t = input()
            mov = 0
        return mov


m = Maze()
p = Player()

# TEST
win = 0
while (win == 0):
    m.printMaze(p)  # Muestro
    direction = m.IAmove(p.xPos, p.yPos)
    while (direction != 0):  # Mientras me pueda mover a caminos desconocidos y libres
        m.addKnownCell(p.xPos, p.yPos)  # Agrego conocidos
        m.addTrueCell(p.xPos, p.yPos)  # Agrego verdaderos
        # Efectivamente me muevo
        if (direction == 1):
            p.moveUp()
            print("p se mueve arriba")
            t = input()
        elif (direction == 2):
            p.moveRight()
            print("p se mueve a la der")
            t = input()
        elif (direction == 3):
            p.moveDown()
            print("p se mueve abajo")
            t = input()
        elif (direction == 4):
            p.moveLeft()
            print("p se mueve a la izq")
            t = input()
        if (m.gameOver(p)):
            win = 1
        m.printMaze(p)  # Muestro
        # Veo donde me muevo
        direction = m.IAmove(p.xPos, p.yPos)
        print(direction, " despues de actualizar")
        test = input()
    print("Nos trabamos")
    test = input()
    m.popTrue()

    # Mientras no encuentre nueva casilla desconocida
    while (win == 0) and (m.IAmove(p.xPos, p.yPos) == 0):
        print("WHILE DE WIN == 0")
        test = input
        cell = {}
        cell = m.popTrue()
        p.moveToPos(cell["x"], cell["y"])

"""
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
"""
