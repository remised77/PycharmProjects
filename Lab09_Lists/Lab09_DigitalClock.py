#
# Written by: Luke Shannon
# 01/29/19
# This program creates a digital clock.

from Lab09_Button import *
from Lab09_graphics import *


class Cell:

    """ This is the description. """

    def __init__(self, center, orientation=False):
        self.center = center
        self.orientation = orientation
        if self.orientation:
            x = self.center.getX()
            y = self.center.getY()
            self.cell = Polygon(Point(x+45, y), Point(x+40, y+5), Point(x-40, y+5),
                                Point(x-45, y), Point(x-40, y-5), Point(x+40, y-5))
        else:
            y = self.center.getX()
            x = self.center.getY()
            self.cell = Polygon(Point(x+45, y), Point(x+40, y+5), Point(x-40, y+5),
                                Point(x-45, y), Point(x-40, y-5), Point(x+40, y-5))

    def fill(self):
        self.cell.fill('black')

    def unfill(self):
        self.cell.fill('white')
        self.cell.setOutline('white')

class Digit:

    """ This is the description. """

    def __init__(self, cellList):
        self.cellList = cellList
        self.numberList =  {0 : [0, 1, 2, 3, 4, 5], 1 : [1, 2], 2: [0, 1, 6, 4, 3], 3 : [0, 1, 6, 2, 3],
                            4 : [5, 6, 1, 2], 5 : [0, 5, 6, 2, 3], 6: [0, 5, 6, 2, 3, 4], 7 : [0, 1, 2],
                            8 : [0, 1, 2, 3, 4, 5, 6], 9 : [0, 1, 2, 5, 6]}

    def setTime(self, number):
        cellsToFill = self.numberList(number)
        for num in cellsToFill:
            eval('cell'+str(num)).fill()

class GUI:

    """ This is the description. """

    def __init__(self):
        self.win = GraphWin('Alarm Clock', 600, 500)
        self.outside = Rectangle(Point(50, 50), Point(550, 200))
        self.entry = Entry(Point(300, 225), 20)
        self.upHour = Button(self.win, Point(50, 350), 100, 40, '+ HOUR', 'black')
        self.downHour = Button(self.win, Point(50, 420), 100, 40, '- HOUR', 'black')
        self.upMinute = Button(self.win, Point(200, 350), 100, 40, '+ MINUTE', 'black')
        self.downMinute = Button(self.win, Point(200, 420), 100, 40, '- MINUTE', 'black')
        self.change = Button(self.win, Point(350, 350), 100, 40, 'CHANGE', 'black')
        self.quit = Button(self.win, Point(350, 420), 100, 40, 'QUIT', 'black')

    def

def initializeDigits():
    for thing in '':
        print ('hi')

def main():
    gui = GUI()
    initializeDigits()
