#
# Written by: Luke Shannon
# 11/27/18
#
# This module creates and controls the fish object for use in SharkRunner..

from graphics import *
from random import *

class fish:
    
    ''' This class creates and controls the fish object for use in SharkRunner.
    List of Methods and Parameters:
    __init__(self, pointFish, direction, pointShark)
    checkWallFlee(self):
    checkWallNonFlee(self):
    move(self, sPoint, fishP1, fishP2):
    checkFlee(self, sharkPoint):
    returnFlee(self):
    returnDirection(self):
    returnPoint(self):
    setEaten(self, boolean):'''

    def __init__(self, pointFish, direction):
        # This method creates the initial fish values, its point and direction.
        self.x = pointFish.getX()
        self.y = pointFish.getY()
        # Our grid for the fish uses integers from 0 - 9 starting from the top left.
        # (0,0) (1,0) (2,0)
        # (0,1) (1,1) (2,1)
        # (0,2) (1,2) (2,2)
        self.direction = direction
        # Our directions are cardinal, using 0 to 3 clockwise around the compass.
        #    0
        # 3  X  1
        #    2
        self.flee = False
        # The fish has not been eaten.
        self.eaten = False
        # Fleeing will be determined in the next move.

    def move(self, sPoint, fishP1, fishP2):
        # This method is main function of fish, to move.
        # First, we establish whether or not the fish is fleeing, by calling checkFlee().
        self.checkFlee(sPoint)
        # Now, we call the function checkWallNonFlee in case the fish is not fleeing.
        # The checkWall functions are separated because there are two cases for checking a wall, if it is fleeing, then
        # it must pass through the wall, and if it is not fleeing, then it must turn around. So the nonFlee version must
        # be called before the movement, while the flee version is called after the movement.
        self.checkWallNonFlee()
        # Now the fish is facing the correct direction if it is not fleeing.
        # So these if statements move the fish one space according to its direction.
        if self.direction == 0:
            self.y += -1
            # This subset of if statements check if the fish is now on top of another fish after the change in position.
            if self.x == fishP1.getX() and self.y == fishP1.getY():
                # If it is, then we reverse the movement, so that no two fish are ever on top of each other.
                self.y += 1
            if self.x == fishP2.getX() and self.y == fishP2.getY():
                self.y += 1
        # This is repeated for all directions.
        elif self.direction == 1:
            self.x += 1
            if self.x == fishP1.getX() and self.y == fishP1.getY():
                self.x += -1
            if self.x == fishP2.getX() and self.y == fishP2.getY():
                self.x += -1
        elif self.direction == 2:
            self.y += 1
            if self.x == fishP1.getX() and self.y == fishP1.getY():
                self.y += -1
            if self.x == fishP2.getX() and self.y == fishP2.getY():
                self.y += -1
        elif self.direction == 3:
            self.x += -1
            if self.x == fishP1.getX() and self.y == fishP1.getY():
                self.x += 1
            if self.x == fishP2.getX() and self.y == fishP2.getY():
                self.x += 1
        else:
            print('direction error')
        # If the fish is in flee mode, then we did not do the checkWallNonFlee above, and now perform checkWallFlee.
        self.checkWallFlee()
        # Return the new location of the fish for use in SharkRunner.
        return Point(self.x, self.y)

    def checkFlee(self, sharkPoint):
        # This function checks whether the shark is close enough that the fish should be in flee mode.
        # X and Y are the distance from the fish to the shark.
        x = self.x - sharkPoint.getX()
        y = self.y - sharkPoint.getY()
        # If both the x and y distance is between 3 units, (or the fish is already fleeing) then the fish should flee.
        if (x <= 3 and x >= -3) and (y <= 3 and y >= -3) or self.flee:
            self.flee = True
        # Otherwise it should not flee.
        else:
            self.flee = False
        # If does enter flee mode, then its direction should change so that it is running directly away from the shark.
        if self.flee:
            # If the absolute value of x and y are the same, then the fish is on a diagonal from the shark.
            if abs(x) == abs(y):
                # If both x and y distances are negative, meaning that the fish is in the top left corner of the shark's
                # 'flee zone,' then the fish should flee N or W, or 0 and 3 respectively as we have denoted them.
                if x<0 and y<0:
                    self.direction = randrange(2)*3
                # If the fish is in the top right corner, it should flee to N or E, 0 or 1.
                elif x>0 and y<0:
                    self.direction = randrange(2)
                # If the fish is in the bottom right corner, it should flee to E or S, 1 or 2.
                elif x>0 and y>0:
                    self.direction = randrange(2)+1
                # If the fish is in the bottom left corner, it should flee to the S or W, 2 or 3.
                elif x<0 and y>0:
                    self.direction = randrange(2)+2
                # Otherwise, raise an error.
                else:
                    print('error')
            # If the fish is not on a diagonal... (see table).
            else:
                # And the x is greater than the y, then the fish must be in the top right half of the flee zone.
                if x>y:
                    # And if the abs(x) < abs(y) on the top right half then the fish is on the top quarter of the zone.
                    if abs(x) < abs(y):
                        self.direction = 0
                    # Otherwise it is in the right quarter of the zone
                    elif abs(x) > abs(y):
                        self.direction = 1
                    else:
                        print('error1')
                # If x < y...
                else:
                    # And abs(x) < abs(y), then the fish is in the bottom quarter of the zone.
                    if abs(x) < abs(y):
                        self.direction = 2
                    # Otherwise it is in the left quarter of the zone.
                    elif abs(x) > abs(y):
                        self.direction = 3
                    else:
                        print('error2')

    def checkWallNonFlee(self):
        # This function checks if there is a wall in front of the fish while it is not fleeing.
        if not self.flee:
            # If the fish is on and is facing the W wall, we must change its direction to E.
            if self.x == 0 and self.direction == 3:
                self.direction = 1
            # If the fish is on and is facing the E wall, we must change its direction to W.
            elif self.x == 9 and self.direction == 1:
                self.direction = 3
            # If the fish is on and is facing the N wall, we must change its direction to S.
            elif self.y == 0 and self.direction == 0:
                self.direction = 2
            # If the fish is on and facing the S wall, we must change its direction to N.
            elif self.y == 9 and self.direction == 2:
                self.direction = 0
            else:
                None

    def checkWallFlee(self):
        # This function checks if the fish has moved through a wall while fleeing.
        # Only exectutes if the fish is fleeing
        if self.flee:
            # If the fish has moved out of the 0-9 grid...
            if self.x < 0:
                # Then we add or subtract 10 to put it back on the other side.
                self.x += 10
                # And turn off flee mode.
                self.flee = False
            # This is repeated for all directions.
            elif self.x > 9:
                self.x += -10
                self.flee = False
            elif self.y < 0:
                self.y += 10
                self.flee = False
            elif self.y > 9:
                self.y += -10
                self.flee = False
            else:
                None

    def setEaten(self, boolean):
        # This function is called when a fish is eaten.
        # It sets the value of the fish as eaten.
        self.eaten = boolean
        # And moves the fish far out of the grid. The fish will continue to move, but the shark will no longer
        # prioritize it as it is too far away. Once all three fish are eaten, the game ends.
        self.x = 10000
        self.y = 10000

    # The following functions return the values of the variables stored in each fish for use in SharkRunner.
    def returnFlee(self):
        return self.flee

    def returnDirection(self):
        return self.direction

    def returnPoint(self):
        return Point(self.x, self.y)