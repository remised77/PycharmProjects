#NAME: NATALIE BREWSTER
#LAB 07: SHARK 
#DATE: 12/2/18
#Send new shark coordinates
import math
from graphics import *

class shark:

    """1. shark finds closest fish with distance formula and compare 4 corners of shark and fish boxes to find shortest distance to shortest fish
    2. enter one of three methods *prelimLine: where shark within eating distance, shark is in a straight line direction away, and diagonal
    3. return shark point only for all conditions"""

    #call class once and then use functions for the rest of the program
    def __init__(self, shark, fish1, fish2, fish3):
        self.shark = shark
        self.fish1 = fish1
        self.fish2 = fish2
        self.fish3 = fish3

    #### HELPER FUNCTIONS ########
    def moveShark(self,shark,fish1,fish2,fish3):
        #put all of the distances from the shark to the fish in a list
        #find smallest fish to shark distance and save that fish as "smallestfish"
        fishDistances = [math.sqrt((shark.getX() - fish1.getX())**2 + (shark.getY() - fish1.getY())**2), math.sqrt((shark.getX() - fish2.getX())**2 + (shark.getY() - fish2.getY())**2), math.sqrt((shark.getX() - fish3.getX())**2 + (shark.getY() - fish3.getY())**2)]
        smallestfishDist = min(fishDistances)
        smallestFish = fishDistances.index(min(fishDistances)) + 1 
        if smallestFish == 1:
            smallestFish = fish1
        elif smallestFish == 2:
            smallestFish = fish2
        else:
            smallestFish = fish3

        #set inital distance to be really long
        shark2fish = 30
        
        #draw all possible line combinations between shark and fish corners. save shortest corner to corner line
        #save shark corner, fish corner, x and y distance, and actual distance
        for i in range(4):
            if i == 0:
                fishTrial = Point(smallestFish.getX(), smallestFish.getY())
            if i == 1:
                fishTrial = Point(smallestFish.getX() + 1, smallestFish.getY())
            if i == 2:
                fishTrial = Point(smallestFish.getX(), smallestFish.getY() + 1)
            if i == 3:
                fishTrial = Point(smallestFish.getX() + 1, smallestFish.getY() + 1)
            for j in range(4):
                if j == 0:
                    sharkTrial = Point(shark.getX(), shark.getY())
                if j == 1:
                    sharkTrial = Point(shark.getX(), shark.getY() + 1)
                if j == 2:
                    sharkTrial = Point(shark.getX() + 1, shark.getY())
                if j == 3:
                    sharkTrial = Point(shark.getX() + 1, shark.getY() + 1)

                #constantly update all new information relating to the shortest line
                if math.sqrt((sharkTrial.getX() - fishTrial.getX())**2 + (sharkTrial.getY() - fishTrial.getY())**2) < shark2fish:
                    shark2fishLINE = Line(sharkTrial,fishTrial)
                    shark2fish = math.sqrt((sharkTrial.getX() - fishTrial.getX())**2 + (sharkTrial.getY() - fishTrial.getY())**2)
                    xDist = sharkTrial.getX() - fishTrial.getX()
                    yDist = sharkTrial.getY() - fishTrial.getY()
                    sharkCoords = sharkTrial
                    fishCoords = fishTrial
                    
        return shark2fish, smallestFish, xDist, yDist, sharkCoords, fishCoords

    def sharkEat(self, smallestFish):
        #move shark to coordinate where the closest fish is
        shark = smallestFish
        return shark
    
    def sharkLine(self,smallestFish,xDist,yDist,sharkCoords,fishCoords):
        #if the shortest distance is a line check which x or y value is not 0
        #if negative difference move less spaces than when positive
        # for special cases, add 1 to x or y *explained in presentation
        
        if xDist == 0:
            if yDist < 0:
                if sharkCoords.getX() - smallestFish.getX() == 1:
                    shark = Point(sharkCoords.getX() - 1, sharkCoords.getY() + 1)
                    return shark
                shark = Point(sharkCoords.getX(), sharkCoords.getY() + 1)
                return shark  
            else:
                if sharkCoords.getX() - smallestFish.getX() == 1:
                    shark = Point(sharkCoords.getX() - 1, sharkCoords.getY() - 2)
                    return shark
                shark = Point(sharkCoords.getX(), sharkCoords.getY() - 2)
                return shark
                              
        if yDist == 0:
            if xDist < 0:
                if sharkCoords.getY() - smallestFish.getY() == 1:
                    shark = Point(sharkCoords.getX() + 1, sharkCoords.getY() - 1)
                    return shark
                shark = Point(sharkCoords.getX() + 1, sharkCoords.getY())
                return shark
            else:
                if sharkCoords.getY() - smallestFish.getY() == 1:
                    shark = Point(sharkCoords.getX() - 2, sharkCoords.getY() - 1)
                    return shark
                shark = Point(sharkCoords.getX() - 2, sharkCoords.getY())
                return shark
            
    def sharkDiag(self,sharkCoords,fishCoords):
        """find equation for line between shark and fish. place a test value into the line to see if the incrument
        is going towards the fish or away from the fish. keep pluging in points and calculating distance from shark
        and point on the line till the length is slightly over sqrt(2) ... 1.45. once at 1.45 save coordinate and find
        what box the coordinate is in and place shark in that box. Logic: circle radius at corner closest to the fish
        will always be the furthest distance the shark can move. """
        #find distance and slope of the line created between two closest fish and shark coordinates
        fishSharkDistance = math.sqrt((sharkCoords.getX() - fishCoords.getX())**2 + (sharkCoords.getY() - fishCoords.getY())**2)
        radius = 0
        m = (sharkCoords.getY() - fishCoords.getY()) / (sharkCoords.getX() - fishCoords.getX())
        # y = mx + b
        b = fishCoords.getY() - m * fishCoords.getX()
        x2 = sharkCoords.getX() + 0.5
        y2 = m * x2 + b

        #check which way on the line it is going, go the other way if going away from fish
        pointD = Point(x2,y2)
        if fishSharkDistance > math.sqrt((fishCoords.getX() - x2)**2 + (fishCoords.getY() - y2)**2):
            mini = 0.1
        else:
            mini = -0.1

        x2 = sharkCoords.getX()
        y2 = m * x2 + b

        #constantly put in slightly higher or lower values till roughly over root 2 away
        while radius <= 1.45: 
            radius = math.sqrt((sharkCoords.getX() - x2)**2 + (sharkCoords.getY() - y2)**2)
            pointD = Point(x2,y2)
            x2 += mini
            y2 = m * x2 + b

            #once it is close to root 2 stop at the intersection of circle and line. locate which square
            if radius >= 1.45:
                shark = Point(pointD.getX()//1,pointD.getY()//1)
                return shark
            
    #use this function to decide which method to use. always returns correct new shark point
    def getShark(self,fish1,fish2,fish3):
        shark = self.shark

        prelimLine = self.moveShark(shark,fish1,fish2,fish3)
        #returned values from prelimLines: shark2fish, smallestFish, xDist, yDist, sharkCoords, fishCoords
        #shark2fish = distance between top left shark and top left fish
        #smallest fish = top left point of fish closest
        # shark coords and fish coords = coordinates that are closets between the fish and shark boxes, xDist yDist are values 

        #if 1 square away
        if prelimLine[0] <= 1.42:
            self.shark = self.sharkEat(prelimLine[1])

        #if directly across
        elif prelimLine[2] == 0 or prelimLine[3] == 0:
            self.shark = self.sharkLine(prelimLine[1],prelimLine[2], prelimLine[3], prelimLine[4],prelimLine[5])
            
        #if some type of diagonal away
        else:
            self.shark = self.sharkDiag(prelimLine[4], prelimLine[5])

    #used in shark runner to collect shark point
    def returnShark(self):
        return(self.shark)
    

