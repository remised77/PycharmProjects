#
#
#
#

from graphics import *

class Tank:

    def __init__(self, color, center, win):
        self.color = color
        self.win = win
        self.center = center
        self.body = Rectangle(Point(center.getX() - 15, center.getY() - 5), Point(center.getX() + 15, center.getY() + 5))
        self.body.fill(self.color)
        self.body.draw(win)


class Ground:

    def __init__(self):
        self.groundList = []

def main():
    win = GraphWin('Tank', 1400, 800)


main()

