# NAME: NATALIE BREWSTER
# LAB 07: SHARK GUI
# DATE: 11/27/18
# Send fish coordinates
from graphics import *
from Button import *
import math
import random


def randDirect():
    numDirect = random.randrange(4)
    if numDirect == 0:
        return "goldfishN.png"
    if numDirect == 1:
        return "goldfishE.png"
    if numDirect == 2:
        return "goldfishS.png"
    if numDirect == 3:
        return "goldfishW.png"

def start():

    win = GraphWin("Shark Game", 1200, 800)
    win.setCoords(-500, -400, 500, 400)
    win.setBackground("white")
    title = Text(Point(0, 50), "S H A R K   G A M E")
    title.setTextColor(color_rgb(0, 142, 204))
    title.setStyle("bold")
    title.setSize(36)
    title.draw(win)
    startButton = Button(win, Point(-50, -50), 120, 40, "START", color_rgb(176, 223, 229))
    startButton.activate()

    userClick = Point(-200, -200)
    while not startButton.clicked(userClick) == True:
        userClick = win.getMouse()

    while startButton.clicked(userClick) == True:
        title.undraw()
        win.setCoords(-1, 11, 17, -1)
        ocean = Rectangle(Point(0, 0), Point(10, 10))
        ocean.setFill(color_rgb(137, 207, 240))
        ocean.draw(win)

        # draw buttons and text
        moveButton = Button(win, Point(12.5, 5), 2, 0.5, "MOVE FISH", color_rgb(176, 223, 229))
        quitButton = Button(win, Point(12.5, 7), 2, 0.5, "QUIT", "light grey")
        quitButton.activate()
        if quitButton.clicked(userClick) == True:
            h = 1/0
        if not (quitButton.clicked(userClick) == True):

            labelCount = 0

            for i in range(11):
                if i == 0 or i == 10:
                    gridY = Rectangle(Point(i - 0.05, -0.05), Point(i + 0.05, 10.05))
                    gridY.setFill(color_rgb(14, 77, 146))
                    gridY.setOutline(color_rgb(14, 77, 146))
                    gridY.draw(win)
                else:
                    gridY = Rectangle(Point(i - 0.05, 0), Point(i + 0.05, 10))
                    gridY.setFill(color_rgb(0, 142, 204))
                    gridY.setOutline(color_rgb(0, 142, 204))
                    gridY.draw(win)

            for j in range(11):
                if j == 0 or j == 10:
                    gridX = Rectangle(Point(-0.05, j - 0.05), Point(10.05, j + 0.05))
                    gridX.setFill(color_rgb(14, 77, 146))
                    gridX.setOutline(color_rgb(14, 77, 146))
                    gridX.draw(win)
                else:
                    gridX = Rectangle(Point(0.05, j - 0.05), Point(9.95, j + 0.05))
                    gridX.setFill(color_rgb(0, 142, 204))
                    gridX.setOutline(color_rgb(0, 142, 204))
                    gridX.draw(win)

            title = Text(Point(13.5, 2), "S H A R K   G A M E")
            title.setTextColor(color_rgb(0, 142, 204))
            title.setStyle("bold")
            title.setSize(36)
            title.draw(win)

            threeFishInfo = Text(Point(13.5, 3), "Click grid to place fish")
            threeFishInfo.setTextColor(color_rgb(14, 77, 146))
            threeFishInfo.setStyle("bold")
            threeFishInfo.setSize(24)
            threeFishInfo.draw(win)

            sharkPNG = Image(Point(7.5, 2.5), "sharkR.png")
            sharkPNG.draw(win)
            shark = Point(7, 2)

            # when inside of a square clicked draw fish
            fishCount = 0
            while fishCount != 3:
                userClick = win.getMouse()
                if quitButton.clicked(userClick) == True:
                    win.close()
                    h = 1/0
                if userClick.getX() >= 0 and userClick.getX() <= 10:
                    if userClick.getY() >= 0 and userClick.getY() <= 10:
                        fishCount += 1

                        if fishCount == 1:
                            x = randDirect()
                            Fish1PNG = Image(
                                Point((userClick.getX() // 1) + 0.5, (userClick.getY() // 1) + 0.5), x)
                            Fish1PNG.draw(win)
                            fish1 = Point(userClick.getX() // 1, userClick.getY() // 1)
                            fishDirect1 = 1
                        if fishCount == 2:
                            x =randDirect()
                            Fish2PNG = Image(
                                Point((userClick.getX() // 1) + 0.5, (userClick.getY() // 1) + 0.5), x)
                            Fish2PNG.draw(win)
                            fish2 = Point(userClick.getX() // 1, userClick.getY() // 1)
                            fishDirect2 = 2
                        if fishCount == 3:
                            x = randDirect()
                            Fish3PNG = Image(
                                Point((userClick.getX() // 1) + 0.5, (userClick.getY() // 1) + 0.5),
                                x)
                            Fish3PNG.draw(win)
                            fish3 = Point(userClick.getX() // 1, userClick.getY() // 1)
                            fishDirect3 = 3

            moveButton.activate()
            threeFishInfo.undraw()
            fish1 = fish1
            fish2 = fish2
            fish3 = fish3

    return fish1, fish2, fish3, fishDirect1, fishDirect2, fishDirect3

'''
    # draw grid, but make lines on the outside darker
for i in range(11):
    if i == 0 or i == 10:
        gridY = Rectangle(Point(i - 0.05, -0.05), Point(i + 0.05, 10.05))
        gridY.setFill(color_rgb(14, 77, 146))
        gridY.setOutline(color_rgb(14, 77, 146))
        gridY.draw(win)
    else:
        gridY = Rectangle(Point(i - 0.05, 0), Point(i + 0.05, 10))
        gridY.setFill(color_rgb(0, 142, 204))
        gridY.setOutline(color_rgb(0, 142, 204))
        gridY.draw(win)

for j in range(11):
    if j == 0 or j == 10:
        gridX = Rectangle(Point(-0.05, j - 0.05), Point(10.05, j + 0.05))
        gridX.setFill(color_rgb(14, 77, 146))
        gridX.setOutline(color_rgb(14, 77, 146))
        gridX.draw(win)
    else:
        gridX = Rectangle(Point(0.05, j - 0.05), Point(9.95, j + 0.05))
        gridX.setFill(color_rgb(0, 142, 204))
        gridX.setOutline(color_rgb(0, 142, 204))
        gridX.draw(win)
'''
'''
    def getInitials(self):
        return initials

    """methods returning values for fish coords color and direction"""

    def randDirect(self):
        numDirect = random.randrange(4)
        if numDirect == 0:
            randDirection = "goldfishN.png"
        if numDirect == 1:
            randDirection = "goldfishE.png"
        if numDirect == 2:
            randDirection = "goldfishS.png"
        if numDirect == 3:
            randDirection = "goldfishW.png"

    def getFish(self, fish):
        if fish == 1:
            return fish1
        if fish == 2:
            return fish2
        if fish == 3:
            return fish3

    def drawShark(self, shark):
        sharkPNG.undraw()
        sharkPNG = Image(Point(shark.getX() + .5, shark.getY() + .5), 'sharkR.png')
        sharkPNG.draw(win)

    # 0-N, 1-E, 2-S, 3-W
    def fleeDirect(self, fish, fishCoords, changeColor, changeDirect):
        if fish == 1:
            fish1 = fishCoords
            if changeColor == False:
                if changeDirect == 0:
                    fishDirect1 = "goldfishN.png"
                if changeDirect == 1:
                    fishDirect1 = "goldfishE.png"
                if changeDirect == 2:
                    fishDirect1 = "goldfishS.png"
                if changeDirect == 3:
                    fishDirect1 = "goldfishW.png"
            if changeColor == True:
                if changeDirect == 0:
                    fishDirect1 = "goldfishN.png"
                if changeDirect == 1:
                    fishDirect1 = "goldfishE.png"
                if changeDirect == 2:
                    fishDirect1 = "goldfishS.png"
                if changeDirect == 3:
                    fishDirect1 = "goldfishW.png"
            fish1PNG = Image(fishCoords, fishDirect1)
            if not fish1.getEaten():
                fish1PNG.draw(win)

        elif fish == 2:
            fish1 = fishCoords
            if changeColor == False:
                if changeDirect == 0:
                    fishDirect2 = "goldfishN.png"
                if changeDirect == 1:
                    fishDirect2 = "goldfishE.png"
                if changeDirect == 2:
                    fishDirect2 = "goldfishS.png"
                if changeDirect == 3:
                    fishDirect2 = "goldfishW.png"
            if changeColor == True:
                if changeDirect == 0:
                    fishDirect2 = "goldfishN.png"
                if changeDirect == 1:
                    fishDirect2 = "goldfishE.png"
                if changeDirect == 2:
                    fishDirect2 = "goldfishS.png"
                if changeDirect == 3:
                    fishDirect2 = "goldfishW.png"
            fish2PNG = Image(fishCoords, fishDirect2)
            if not fish2.getEaten():
                fish2PNG.draw(win)

        else:
            fish3 = fishCoords
            if changeColor == False:
                if changeDirect == 0:
                    fishDirect3 = "goldfishN.png"
                if changeDirect == 1:
                    fishDirect3 = "goldfishE.png"
                if changeDirect == 2:
                    fishDirect3 = "goldfishS.png"
                if changeDirect == 3:
                    fishDirect1 = "goldfishW.png"
            if changeColor == True:
                if changeDirect == 0:
                    fishDirect3 = "goldfishNF.png"
                if changeDirect == 1:
                    fishDirect3 = "goldfishEF.png"
                if changeDirect == 2:
                    fishDirect3 = "goldfishSF.png"
                if changeDirect == 3:
                    fishDirect3 = "goldfishWF.png"
            fish3PNG = Image(fishCoords, fishDirect3)
            if not fish3.getEaten():
                fish3PNG.draw(win)

    def getDirect(self, fish):
        if fish == 1:
            return fishDirect1
        if fish == 2:
            return fishDirect2
        if fish == 3:
            return fishDirect3

    def setDirect(self, fish):
        return None

    def changeLabel(self):
        labelCount += 1

    def fishGone(self):
        threeFishInfo = Text(Point(13.5, 3), "All fish eaten! Try again?")
        threeFishInfo.setTextColor(color_rgb(14, 77, 146))
        threeFishInfo.setStyle("bold")
        threeFishInfo.setSize(24)
        threeFishInfo.draw(win)

    ##########################
    def createGrid(self):
        # draw grid, but make lines on the outside darker
        for i in range(11):
            if i == 0 or i == 10:
                gridY = Rectangle(Point(i - 0.05, -0.05), Point(i + 0.05, 10.05))
                gridY.setFill(color_rgb(14, 77, 146))
                gridY.setOutline(color_rgb(14, 77, 146))
                gridY.draw(win)
            else:
                gridY = Rectangle(Point(i - 0.05, 0), Point(i + 0.05, 10))
                gridY.setFill(color_rgb(0, 142, 204))
                gridY.setOutline(color_rgb(0, 142, 204))
                gridY.draw(win)

        for j in range(11):
            if j == 0 or j == 10:
                gridX = Rectangle(Point(-0.05, j - 0.05), Point(10.05, j + 0.05))
                gridX.setFill(color_rgb(14, 77, 146))
                gridX.setOutline(color_rgb(14, 77, 146))
                gridX.draw(win)
            else:
                gridX = Rectangle(Point(0.05, j - 0.05), Point(9.95, j + 0.05))
                gridX.setFill(color_rgb(0, 142, 204))
                gridX.setOutline(color_rgb(0, 142, 204))
                gridX.draw(win)

    def waitClick(self):
        userClick = win.getMouse()
        while not quitButton.clicked(userClick):
            if moveButton.clicked(userClick):
                return True
            userClick = win.getMouse()
        win.close()

    def checkQuitClicked(self, click):
        return quitButton.clicked(click)

    def getClick(self):
        userClick = win.getMouse()
        return (userClick)

    def checkMoveClicked(self):
        return moveButton.clicked(click)

    #  while quitButton.clicked(userClick) == True:
    #     return False
    # while not quitButton.clicked(userClick) == True:
#           if quitButton.clicked(userClick) == True:
#              return False
#         while not startButton.clicked(userClick) == True:
#            if quitButton.clicked(userClick) == True:
#               return False
#          userClick = win.getMouse()
#
#           while startButton.clicked(userClick) == True:
#              return True'''


