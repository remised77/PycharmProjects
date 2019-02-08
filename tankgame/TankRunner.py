#
#
#
#

from graphics import *
from math import *


class Tank:

    def __init__(self, color, center, gui):
        self.color = color
        self.gui = gui
        self.center = center
        self.body = Rectangle(Point(center.getX() - 15, center.getY() - 5), Point(center.getX() + 15, center.getY() + 5))
        self.body.setFill(self.color)
        self.body.draw(self.gui.win)

    def move_tank(self):
        range = Circle(self.center, 400)
        range.draw(self.gui.win)
        range.setOutline('green')
        point = self.gui.win.getMouse()
        while sqrt((point.getX() - self.center.getX())**2 + (point.getY() - self.center.getX() < 50)**2) > 400:
            point = self.gui.win.getMouse()
        dx = point.getX() - self.center.getX()
        dy = point.getY() - self.center.getY()
        self.body.move(dx, dy)
        self.center = Point(self.center.getX() + dx, self.center.getY() + dy)
        range.undraw()


class GUI:

    def __init__(self):
        self.win = GraphWin('Tank', 1400, 800)

    def splode(self, hit):
        splosion = Circle(hit, 50)
        splosion.setFill('white')
        splosion.setOutline('white')
        splosion.draw(self.win)


class Ground:

    def __init__(self, gui):
        self.gui = gui
        for x in range(0, 1401):
            for y in range(400, 801):
                point = Point(x, y)
                point.setOutline('green')
                point.draw(self.gui.win)


    def bomb(self, hit):
        x=1


class Physics:

    def __init__(self, gui):
        self.gui = gui

    def fall(self, point, speed):
        if x:
            x=1


    def projectile(self):
        x=1


class User:

    def __init__(self, gui):
        self.gui = gui
        self.g = -9.8

    def projectile(self, point, x_velocity, y_velocity):
        x=1


def main():
    gui = GUI()
    ground = Ground(gui)
    phys = Physics(gui)
    tank1 = Tank('red', Point(200, 300), gui)
    tank2 = Tank('blue', Point(1200, 300), gui)
    ground.bomb(Point(800, 400))
    tank1.move_tank()
    x = Point(10,700)
    #gui.win.plot(10, 700, 'red')
    x.setFill('red')
    x.draw(gui.win)
    print(x.config['outline'])
    gui.win.getMouse()


main()

