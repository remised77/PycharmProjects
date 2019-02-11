# File: Lab10_PieceClass.py
# Written by Remi Seddigh and Luke Shannon
# 2019–02–09
# Square class for each square on the chessboard

from graphics import *
from math import *

class Square:

    def __init__(self, square_string, color, length):

        self.name = square_string

        self.length = length

        x = ord(self.name[0]) - 96
        y = int(self.name[1])

        self.color = color

        self.location = Point(x, y)

        self.xmin = self.location.getX()-(self.length/2)
        self.ymin = self.location.getY() - (self.length / 2)

        self.rect = Rectangle(Point(xmin, ymin), Point(xmin+length, ymin+length))



    def clicked(self, p):

        return (self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

