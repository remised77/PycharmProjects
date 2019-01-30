#NAME: NATALIE BREWSTER
#LAB 07: SHARK GUI
#DATE: 11/27/18
#Send fish coordinates
from graphics import *
from Button import *
import random

class sharkGUI:

    def __init__(self):
        self.win = GraphWin("Shark Game", 1200, 800)
        self.setUp()

    def setUp(self):
        self.win.setCoords( -500, -400, 500, 400)
        self.win.setBackground("white")
        title = Text(Point(0,50), "S H A R K   G A M E")
        title.setTextColor(color_rgb(0, 142, 204))
        title.setStyle("bold")
        title.setSize(36)
        title.draw(self.win)
        startButton = Button(self.win, Point(-50,-50), 120, 40, "START", color_rgb(176, 223, 229))
        startButton.activate()

        self.userClick = Point(-200,-200)
        while not startButton.clicked(self.userClick) == True:
            self.userClick = self.win.getMouse()

        while startButton.clicked(self.userClick) == True:
            title.undraw()
            self.win.setCoords(-1, 11, 17, -1)
            ocean = Rectangle(Point(0,0), Point(10,10))
            ocean.setFill(color_rgb(137, 207, 240))
            ocean.draw(self.win)

            #draw buttons and text         
            self.moveButton = Button(self.win, Point(12.5,5), 2, 0.5, "MOVE FISH", color_rgb(176, 223, 229))
            self.quitButton = Button(self.win, Point(12.5,7), 2, 0.5, "QUIT", "light grey")
            self.quitButton.activate()
            if self.quitButton.clicked(self.userClick) == True:
                h = 1/0
            if not self.quitButton.clicked(self.userClick) == True:

                self.labelCount = 0

                self.createGrid()

                title = Text(Point(13.5,2), "S H A R K   G A M E")
                title.setTextColor(color_rgb(0, 142, 204))
                title.setStyle("bold")
                title.setSize(36)
                title.draw(self.win)

                threeFishInfo = Text(Point(13.5,3), "Click grid to place fish")
                threeFishInfo.setTextColor(color_rgb(14, 77, 146))
                threeFishInfo.setStyle("bold")
                threeFishInfo.setSize(24)
                threeFishInfo.draw(self.win)

                self.sharkPNG = Image(Point(7.5,2.5), "sharkR.gif")
                self.sharkPNG.draw(self.win)
                self.shark = Point(7,2)

                #when inside of a square clicked draw fish
                fishCount = 0
                while fishCount != 3:
                    self.userClick = self.win.getMouse()
                    if self.quitButton.clicked(self.userClick) == True:
                        self.win.close()
                        o = 1/0
                    if self.userClick.getX() >= 0 and self.userClick.getX() <= 10:
                        if self.userClick.getY() >= 0 and self.userClick.getY() <= 10:
                            fishCount += 1

                            if fishCount == 1:
                                self.randDirect()
                                self.fish1PNG = Image(Point((self.userClick.getX()//1)+0.5,(self.userClick.getY()//1)+0.5), self.randDirection)
                                self.fish1PNG.draw(self.win)
                                self.fish1 = Point(self.userClick.getX()//1,self.userClick.getY()//1)
                                fishDirect1 = self.numDirect
                            if fishCount == 2:
                                self.randDirect()
                                self.fish2PNG = Image(Point((self.userClick.getX()//1)+0.5,(self.userClick.getY()//1)+0.5), self.randDirection)
                                self.fish2PNG.draw(self.win)
                                self.fish2 = Point(self.userClick.getX()//1,self.userClick.getY()//1)
                                fishDirect2 = self.numDirect
                            if fishCount == 3:
                                self.randDirect()
                                self.fish3PNG = Image(Point((self.userClick.getX()//1)+0.5,(self.userClick.getY()//1)+0.5), self.randDirection)
                                self.fish3PNG.draw(self.win)
                                self.fish3 = Point(self.userClick.getX()//1,self.userClick.getY()//1)
                                fishDirect3 = self.numDirect

                self.moveButton.activate()
                threeFishInfo.undraw()
                fish1 = self.fish1
                fish2 = self.fish2
                fish3 = self.fish3
                randDirection = self.randDirection
        self.initials = [fish1, fish2, fish3, fishDirect1, fishDirect2, fishDirect3]

    def getInitials(self):
        return self.initials
        
    """methods returning values for fish coords color and direction"""      
    def randDirect(self):
        self.numDirect = random.randrange(4)
        if self.numDirect == 0:
            self.randDirection = "goldfish1N.gif"
        if self.numDirect == 1:
            self.randDirection = "goldfish1E.gif"
        if self.numDirect == 2:
            self.randDirection = "goldfish1S.gif"
        if self.numDirect == 3:
            self.randDirection = "goldfish1W.gif"
            
    def getFish(self, fish):
        if fish == 1:
            return self.fish1
        if fish == 2:
            return self.fish2
        if fish == 3:
            return self.fish3
        
    def drawShark(self, sharkPoint):
        self.sharkPNG.undraw()
        self.sharkPNG = Image(Point(sharkPoint.getX() + .5, sharkPoint.getY() + .5), 'sharkR.gif')
        self.sharkPNG.draw(self.win)

    # 0-N, 1-E, 2-S, 3-W
    def fleeDirect(self, fish, fishCoords, fleeColor, changeDirect):
        self.fish = fish
        self.fleeColor = fleeColor

        if self.fish == 1:
            self.fish1PNG.undraw()
            self.fish1 = fishCoords
            if self.fleeColor == False:
                if changeDirect == 0:
                    self.fishDirect1 = "goldfish1N.gif"
                if changeDirect == 1:
                    self.fishDirect1 = "goldfish1E.gif"
                if changeDirect == 2:
                    self.fishDirect1 = "goldfish1S.gif"
                if changeDirect == 3:
                    self.fishDirect1 = "goldfish1W.gif"
            if self.fleeColor == True:
                if changeDirect == 0:
                    self.fishDirect1 = "goldfish1NF.gif"
                if changeDirect == 1:
                    self.fishDirect1 = "goldfish1EF.gif"
                if changeDirect == 2:
                    self.fishDirect1 = "goldfish1SF.gif"
                if changeDirect == 3:
                    self.fishDirect1 = "goldfish1WF.gif"
            self.fish1PNG = Image(Point(fishCoords.getX()+.5, fishCoords.getY()+.5), self.fishDirect1)
            self.fish1PNG.draw(self.win)

        elif self.fish == 2:
            self.fish2PNG.undraw()
            self.fish2 = fishCoords
            if self.fleeColor == False:
                if changeDirect == 0:
                    self.fishDirect2 = "goldfish1N.gif"
                if changeDirect == 1:
                    self.fishDirect2 = "goldfish1E.gif"
                if changeDirect == 2:
                    self.fishDirect2 = "goldfish1S.gif"
                if changeDirect == 3:
                    self.fishDirect2 = "goldfish1W.gif"
            if self.fleeColor == True:
                if changeDirect == 0:
                    self.fishDirect2 = "goldfish1NF.gif"
                if changeDirect == 1:
                    self.fishDirect2 = "goldfish1EF.gif"
                if changeDirect == 2:
                    self.fishDirect2 = "goldfish1SF.gif"
                if changeDirect == 3:
                    self.fishDirect2 = "goldfish1WF.gif"
            self.fish2PNG = Image(Point(fishCoords.getX()+.5, fishCoords.getY()+.5), self.fishDirect2)
            self.fish2PNG.draw(self.win)
        
        else:
            self.fish3PNG.undraw()
            self.fish3 = fishCoords

            if self.fleeColor == False:
                if changeDirect == 0:
                    self.fishDirect3 = "goldfish1N.gif"
                if changeDirect == 1:
                    self.fishDirect3 = "goldfish1E.gif"
                if changeDirect == 2:
                    self.fishDirect3 = "goldfish1S.gif"
                if changeDirect == 3:
                    self.fishDirect3 = "goldfish1W.gif"
            if self.fleeColor == True:
                if changeDirect == 0:
                    self.fishDirect3 = "goldfish1NF.gif"
                if changeDirect == 1:
                    self.fishDirect3 = "goldfish1EF.gif"
                if changeDirect == 2:
                    self.fishDirect3 = "goldfish1SF.gif"
                if changeDirect == 3:
                    self.fishDirect3 = "goldfish1WF.gif"
            self.fish3PNG = Image(Point(fishCoords.getX()+.5, fishCoords.getY()+.5), self.fishDirect3)
            self.fish3PNG.draw(self.win)
                        
    def getDirect(self,fish):
        if fish == 1:
            return self.fishDirect1
        if fish == 2:
            return self.fishDirect2
        if fish == 3:
            return self.fishDirect3

    def setDirect(self, fish):
        return None

    def changeLabelShark(self):
        self.moveButton.setLabel("Move Shark")

    def changeLabelFish(self):
        self.moveButton.setLabel("Move Fish")

    def fishGone(self,stalemate):
        if stalemate:
            threeFishInfo = Text(Point(13.5,3), "Stalemate: the fish win.")
        else:
            threeFishInfo = Text(Point(13.5, 3), "All fish eaten! Play again?")
        threeFishInfo.setTextColor(color_rgb(14, 77, 146))
        threeFishInfo.setStyle("bold")
        threeFishInfo.setSize(24)
        self.moveButton.setLabel('Again!')
        threeFishInfo.draw(self.win)
        m1 = self.win.getMouse()
        if self.moveButton.clicked(m1):
            self.win.close()
            return True

    ##########################
    def createGrid(self):
    #draw grid, but make lines on the outside darker
        for i in range(11):     
            if i == 0 or i == 10:
                gridY = Rectangle(Point(i-0.05,-0.05), Point(i+0.05,10.05))
                gridY.setFill(color_rgb(14, 77, 146))
                gridY.setOutline(color_rgb(14, 77, 146))
                gridY.draw(self.win)
            else:
                gridY = Rectangle(Point(i-0.05,0), Point(i+0.05,10))
                gridY.setFill(color_rgb(0, 142, 204))
                gridY.setOutline(color_rgb(0, 142, 204))
                gridY.draw(self.win)
            
        for j in range(11):
            if j == 0 or j == 10:
                gridX = Rectangle(Point(-0.05,j-0.05), Point(10.05,j+0.05))
                gridX.setFill(color_rgb(14, 77, 146))
                gridX.setOutline(color_rgb(14, 77, 146))
                gridX.draw(self.win)
            else:
                gridX = Rectangle(Point(0.05,j-0.05), Point(9.95,j+0.05))
                gridX.setFill(color_rgb(0, 142, 204))
                gridX.setOutline(color_rgb(0, 142, 204))
                gridX.draw(self.win)
    def waitClick(self):
        self.userClick = self.win.getMouse()
        while not self.quitButton.clicked(self.userClick):
            if self.moveButton.clicked(self.userClick):
                return True
            self.userClick = self.win.getMouse()
        self.win.close()

    def checkQuitClicked(self, click):
        return self.quitButton.clicked(click)

    def getClick(self):
        self.userClick = self.win.getMouse()
        return(self.userClick)

    def checkMoveClicked(self, click):
        return self.moveButton.clicked(click)

      #  while self.quitButton.clicked(self.userClick) == True:
       #     return False
        #while not self.quitButton.clicked(self.userClick) == True:
 #           if self.quitButton.clicked(self.userClick) == True:
  #              return False
   #         while not startButton.clicked(self.userClick) == True:
    #            if self.quitButton.clicked(self.userClick) == True:
     #               return False
      #          self.userClick = self.win.getMouse()
#
 #           while startButton.clicked(self.userClick) == True:
  #              return True


