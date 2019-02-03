#
# Written by: Luke Shannon
# 01/29/19
# This program creates team rankings.

from Lab09_graphics import *

win = GraphWin('s', 400,400)
l = Line(Point(20,20),Point(100,20))
t = Line(Point(20,20), Point(20,30))
l.draw(win)
t.draw(win)
win.getMouse()

