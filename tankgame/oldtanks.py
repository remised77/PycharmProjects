TankRunner

# Written by: Luke Shannon
# 12/23/18
# The tank game.

from graphics import *
from tank import *
from Ground import *
from health import *
from Ammo import *


def main():
    win = GraphWin('Gamer Guys', 1400, 800)
    win.setBackground('light blue')
    win.setCoords(0, 0, 1400, 800)
    ground = Ground(win)
    tank1 = Tank(Point(200,500), 'blue', win)
    tank2 = Tank(Point(1200,500), 'red', win)
    ground.draw(win)
    tank1.draw()
    tank2.draw()
    while tank1.health > 0 and tank2.health > 0:
    # while no one has won:
        while tank1.fuel > 0 or tank2.fuel > 0:
    #     while tank still has fuel
            key = win.getKey()
    #         check for keys
            if key == 'right':
                if tank1.fuel > 0:
                    tank1.moveR
                if tank2.fuel > 0:
                    tank2.moveR
            if key == 'left':
                if tank1.fuel > 0:
                    tank1.moveL
                if tank2.fuel > 0:
                    tank2.moveL
            if key == 'down':
                tank1.fuel = 0
                tank2.fuel = 0
            if key == 'up':
                if tank1.fuel > 0:
                    tank1.jump
                if tank2.fuel > 0:
                    tank2.jump
    #     while tank has ammo
    #         check for click
    #         if click
    #             fire and trace shell
    #             impact shell
    #             change land
    #             take health
    #             check tanks for falling
    #     check for end of game
    # present winners
    # ask to play again


main()

tank

# Written by: Luke Shannon
# 12/23/18
# The tank class.

from graphics import *


class Tank:

    '''fqwohgl'''

    def __init__(self, create, color, window):
        print(create)
        print(color)
        print(win)
        self.win = window
        self.x = create.getX()
        self.y = create.getY()
        self.color = color
        self.body = Rectangle(Point(self.x - 25, self.y), Point(self.x + 25, self.y + 30))
        self.body = self.body.setFill(self.color)

    def draw(self):
        self.body.draw(self.win)

    def aim(self, point):
        # move gun here
        None

    def move(self, key):
        # move tank
        None

from tank import *
win = GraphWin('', 400, 400)
tank1 = Tank(Point(200,300), 'green', win)

ammo

# Written by: Luke Shannon
# 12/23/18
# The ammo class.

class Ammo:

    def __init__(self, aimed):
        self.aimX = aimed.getX()
        self.aimY = aimed.getY()


ground

# Written by: Luke Shannon
# 12/23/18
# The ground class.

from graphics import *


class Ground:

    def __init__(self, win):
        self.win = win
        self.ground = Polygon(Point(0, 0), Point(0, 300), Point(1400, 300), Point(1400, 0))
        self.ground.setFill('green')
        self.ground.setOutline('green')
        self.groundLines = [500]

    def draw(self, win):
        self.win = win
        self.ground.draw(win)

    def check_ground(self, point):
        x = point.getX()
        y = point.getY()
        lowest = 1600
        for line in self.groundLines:
            height = line
            if height < lowest:
                lowest = height
        if lowest < y + 3 or lowest > y + 3:
            return True
        else:
            return False

    def add_line(self, newLine):
        self.groundLines.append(newLine)


health
# Written by: Luke Shannon
# 12/23/18
# The tank class.

from graphics import *


class Tank:

    def __init__(self, player, name):
        if player:
            health = Rectangle(Point(0,0), Point(0,0))



  for point in self.ground_points:
            if sqrt((hit.getX() - point.getX())**2 + (hit.getY() - point.getX() < 50)**2) < 49:
                self.ground_points.remove(point)
        temp_circle = []
        for x in range(-50, 50):
            y = int(sqrt(50 * 50 - x * x))
            temp_circle.append(Point(int(hit.getX() + x), int(hit.getY() + y)))
            temp_circle.append(Point(int(hit.getX() + x), int(hit.getY() - y)))
        filler = []
        for i in range(0, len(temp_circle)-1):
            for i2 in range(0, int(temp_circle[i+1].getY() - temp_circle[i].getY())):
                filler.append(Point(temp_circle[i].getX(), temp_circle[i].getY()+i2))
        for item in filler:
            temp_circle.append(item)
        intersections = []
        temp_circle = list(set(temp_circle))
        print(temp_circle)
        print(self.ground_points)
        for point in self.ground_points:
            if point in temp_circle:
                intersections.append(point)
        print(intersections)
        for i in range(intersections[0].getX(), intersections[1].getX()):
            for point in self.ground_points:
                if int(point.getX()) == i and point.getY() > 0:
                    self.ground_points.remove(point)
        self.gui.splode(hit)


