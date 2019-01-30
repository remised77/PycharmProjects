#NAME: NATALIE BREWSTER
#LAB 07: SHARK GUI
#DATE: 11/27/18
#Draw starting screen, place inital fish and shark, move fish and shark to new spots
#Control all buttons and notify when eaten / restart
from graphics import *
from Button import *
import random

class sharkGUI:

    def __init__(self):
        self.win = GraphWin("Shark Game", 1200, 800)
        self.startScreen()

    def startScreen(self):
        #draw starting screen 
        self.win.setCoords(-500, -400, 500, 400)
        self.win.setBackground("white")
        self.title = Text(Point(0,50), "S H A R K   G A M E")
        self.title.setTextColor(color_rgb(0, 142, 204))
        self.title.setStyle("bold")
        self.title.setSize(36)
        self.title.draw(self.win)
        startButton = Button(self.win, Point(-50,-50), 120, 40, "START", color_rgb(176, 223, 229))
        startButton.activate()
        
        #wait till user clicks start button
        self.userClick = Point(-200,-200)
        while not startButton.clicked(self.userClick):
            self.userClick = self.win.getMouse()
        self.win.setCoords(-1, 11, 17, -1)


    def setUp(self):
        #
        self.title.undraw()
        #re set coordinates so they line up with grid and math is easier to do
        #draw blue backdrop
        ocean = Rectangle(Point(0,0), Point(10,10))
        ocean.setFill(color_rgb(137, 207, 240))
        ocean.draw(self.win)
        #draw buttons and text
        self.moveButton = Button(self.win, Point(12.5,5), 2, 0.5, "MOVE FISH", color_rgb(176, 223, 229))
        self.quitButton = Button(self.win, Point(12.5,7), 2, 0.5, "QUIT", "light grey")
        self.quitButton.activate()
        if self.quitButton.clicked(self.userClick) == True:
            #division by 0 makes program break
            h = 1/0
        if not self.quitButton.clicked(self.userClick) == True:
            #draw grid and entry text. did grid click function instead of entry boxes
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
            self.sharkGIF = Image(Point(7.5,2.5), "sharkR.gif")
            self.sharkGIF.draw(self.win)
            self.shark = Point(7,2)

            #when a click inside of the grid is detected, place image in square they clicked and save it to a fish value
            #loop stops after 3 fish are placed and buttons are activated
            fishCount = 0
            while fishCount != 3:
                self.userClick = self.win.getMouse()
                if self.quitButton.clicked(self.userClick) == True:
                    self.win.close()
                    o = 1/0
                if self.userClick.getX() >= 0 and self.userClick.getX() <= 10:
                    if self.userClick.getY() >= 0 and self.userClick.getY() <= 10:
                        fishCount += 1
                        #round down the coordinate for where user clicked to get fish coordinate. Place image +.5 in both directions
                        if fishCount == 1:
                            self.randDirect(1)
                            self.fish1GIF = Image(Point((self.userClick.getX()//1)+0.5,(self.userClick.getY()//1)+0.5), self.randDirection)
                            self.fish1GIF.draw(self.win)
                            self.fish1 = Point(self.userClick.getX()//1,self.userClick.getY()//1)
                            fishDirect1 = self.numDirect
                        if fishCount == 2:
                            self.randDirect(2)
                            self.fish2GIF = Image(Point((self.userClick.getX()//1)+0.5,(self.userClick.getY()//1)+0.5), self.randDirection)
                            self.fish2GIF.draw(self.win)
                            self.fish2 = Point(self.userClick.getX()//1,self.userClick.getY()//1)
                            fishDirect2 = self.numDirect
                        if fishCount == 3:
                            self.randDirect(3)
                            self.fish3GIF = Image(Point((self.userClick.getX()//1)+0.5,(self.userClick.getY()//1)+0.5), self.randDirection)
                            self.fish3GIF.draw(self.win)
                            self.fish3 = Point(self.userClick.getX()//1,self.userClick.getY()//1)
                            fishDirect3 = self.numDirect

            self.moveButton.activate()
            threeFishInfo.undraw()
            fish1 = self.fish1
            fish2 = self.fish2
            fish3 = self.fish3
            randDirection = self.randDirection
        self.initials = [fish1, fish2, fish3, fishDirect1, fishDirect2, fishDirect3]
        return None
    
    #function used becuase init can only return none
    def getInitials(self):
        return self.initials
        
    #used only for inital random fish directions at the beginning of the program     
    def randDirect(self,fishNum):
        if fishNum == 1:  
            self.numDirect = random.randrange(4)
            if self.numDirect == 0:
                self.randDirection = "goldfish1N.gif"
            if self.numDirect == 1:
                self.randDirection = "goldfish1E.gif"
            if self.numDirect == 2:
                self.randDirection = "goldfish1S.gif"
            if self.numDirect == 3:
                self.randDirection = "goldfish1W.gif"
        elif fishNum == 2:  
            self.numDirect = random.randrange(4)
            if self.numDirect == 0:
                self.randDirection = "goldfish2N.gif"
            if self.numDirect == 1:
                self.randDirection = "goldfish2E.gif"
            if self.numDirect == 2:
                self.randDirection = "goldfish2S.gif"
            if self.numDirect == 3:
                self.randDirection = "goldfish2W.gif"
        else:  
            self.numDirect = random.randrange(4)
            if self.numDirect == 0:
                self.randDirection = "goldfish3N.gif"
            if self.numDirect == 1:
                self.randDirection = "goldfish3E.gif"
            if self.numDirect == 2:
                self.randDirection = "goldfish3S.gif"
            if self.numDirect == 3:
                self.randDirection = "goldfish3W.gif"
            
    def getFish(self, fish):
        if fish == 1:
            return self.fish1
        if fish == 2:
            return self.fish2
        if fish == 3:
            return self.fish3

    #draws shark in the center of the square
    def drawShark(self, sharkPoint):
        self.sharkGIF.undraw()
        self.sharkGIF = Image(Point(sharkPoint.getX() + .5, sharkPoint.getY() + .5), 'sharkR.gif')
        self.sharkGIF.draw(self.win)

    # 0-N, 1-E, 2-S, 3-W . use function flee direct to: change direction, color, and draw 
    #one function that constantly checks flee makes sharkrunner easier to follow
    def fleeDirect(self, fish, fishCoords, fleeColor, changeDirect):
        self.fish = fish
        self.fleeColor = fleeColor

        if self.fish == 1:
            self.fish1GIF.undraw()
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
            self.fish1GIF = Image(Point(fishCoords.getX()+.5, fishCoords.getY()+.5), self.fishDirect1)
            self.fish1GIF.draw(self.win)

        elif self.fish == 2:
            self.fish2GIF.undraw()
            self.fish2 = fishCoords
            if self.fleeColor == False:
                if changeDirect == 0:
                    self.fishDirect2 = "goldfish2N.gif"
                if changeDirect == 1:
                    self.fishDirect2 = "goldfish2E.gif"
                if changeDirect == 2:
                    self.fishDirect2 = "goldfish2S.gif"
                if changeDirect == 3:
                    self.fishDirect2 = "goldfish2W.gif"
            if self.fleeColor == True:
                if changeDirect == 0:
                    self.fishDirect2 = "goldfish2NF.gif"
                if changeDirect == 1:
                    self.fishDirect2 = "goldfish2EF.gif"
                if changeDirect == 2:
                    self.fishDirect2 = "goldfish2SF.gif"
                if changeDirect == 3:
                    self.fishDirect2 = "goldfish2WF.gif"
            self.fish2GIF = Image(Point(fishCoords.getX()+.5, fishCoords.getY()+.5), self.fishDirect2)
            self.fish2GIF.draw(self.win)
        
        else:
            self.fish3GIF.undraw()
            self.fish3 = fishCoords

            if self.fleeColor == False:
                if changeDirect == 0:
                    self.fishDirect3 = "goldfish3N.gif"
                if changeDirect == 1:
                    self.fishDirect3 = "goldfish3E.gif"
                if changeDirect == 2:
                    self.fishDirect3 = "goldfish3S.gif"
                if changeDirect == 3:
                    self.fishDirect3 = "goldfish3W.gif"
            if self.fleeColor == True:
                if changeDirect == 0:
                    self.fishDirect3 = "goldfish3NF.gif"
                if changeDirect == 1:
                    self.fishDirect3 = "goldfish3EF.gif"
                if changeDirect == 2:
                    self.fishDirect3 = "goldfish3SF.gif"
                if changeDirect == 3:
                    self.fishDirect3 = "goldfish3WF.gif"
            self.fish3GIF = Image(Point(fishCoords.getX()+.5, fishCoords.getY()+.5), self.fishDirect3)
            self.fish3GIF.draw(self.win)

    #functions that change label and color of buttons
    def changeLabelShark(self):
        self.moveButton.setLabel("MOVE SHARK")
        self.moveButton.setColor("light blue")

    def changeLabelFish(self):
        self.moveButton.setLabel("MOVE FISH")
        self.moveButton.setColor("light yellow")

    #print info that player should restart game since all fish are gone
    def fishGone(self,stalemate):
        if stalemate:
            threeFishInfo = Text(Point(13.5, 3.5), "Stalemate: the fish win.")
        else:
            threeFishInfo = Text(Point(13.5, 3.5), "All fish eaten! Play again?")
        threeFishInfo.setTextColor(color_rgb(14, 77, 146))
        threeFishInfo.setStyle("bold")
        threeFishInfo.setSize(24)
        self.moveButton.setLabel('Again!')
        threeFishInfo.draw(self.win)
        m1 = self.win.getMouse()
        if self.moveButton.clicked(m1):
            threeFishInfo.undraw()
            return True

    #draw grid, but make lines on the outside darker
    def createGrid(self):
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
    
    def checkQuitClicked(self, click):
        return self.quitButton.clicked(click)

    def getClick(self):
        self.userClick = self.win.getMouse()
        return(self.userClick)

    def checkMoveClicked(self, click):
        return self.moveButton.clicked(click)

    #message that says which fish has been eaten
    def setMessage(self, message):
        fishEatInfo = Text(Point(13.5,3), message)
        fishEatInfo.setTextColor(color_rgb(14, 77, 146))
        fishEatInfo.setStyle("bold")
        fishEatInfo.setSize(24)
        fishEatInfo.draw(self.win)

    #draw white rectangle over fish info everytime 
    def clearMessage(self):
        fishCover = Rectangle(Point(16.5,2.5),Point(10.5,4))
        fishCover.setFill("white")
        fishCover.setOutline("white")
        fishCover.draw(self.win)
        


