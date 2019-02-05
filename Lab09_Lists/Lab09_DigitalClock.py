#
# Written by: Luke Shannon
# 01/29/19
# This program creates a digital clock.

from Lab09_Button import *
from Lab09_graphics import *


class Cell:

    """ This is the description. """

    def __init__(self, gui, center, orientation='x'):
        self.gui = gui
        self.win = gui.win
        self.center = center
        self.orientation = orientation
        x = self.center.getX()
        y = self.center.getY()
        if self.orientation:
            self.cell = Polygon(Point(x+45, y), Point(x+40, y+5), Point(x-40, y+5),
                                Point(x-45, y), Point(x-40, y-5), Point(x+40, y-5))
        else:
            self.cell = Polygon(Point(x, y-45), Point(x+5, y-40), Point(x+5, y+40),
                                Point(x, y+45), Point(x-5, y+40), Point(x-5, y-40))
        self.cell.setFill('white')
        self.cell.draw(self.win)

    def fill(self):
        self.cell.setFill('black')

    def unfill(self):
        self.cell.setFill('white')


class Digit:

    """ This is the description. """

    def __init__(self, center, gui):
        self.gui = gui
        self.center = center
        self.number = 0

        self.cell0 = Cell(self.gui, Point(center.getX(), center.getY() - 90))
        self.cell1 = Cell(self.gui, Point(center.getX() + 45, center.getY() - 45), False)
        self.cell2 = Cell(self.gui, Point(center.getX() + 45, center.getY() + 45), False)
        self.cell3 = Cell(self.gui, Point(center.getX(), center.getY() + 90))
        self.cell4 = Cell(self.gui, Point(center.getX() - 45, center.getY() + 45), False)
        self.cell5 = Cell(self.gui, Point(center.getX() - 45, center.getY() - 45), False)
        self.cell6 = Cell(self.gui, Point(center.getX(), center.getY()))

        self.numberList = {0: [0, 1, 2, 3, 4, 5],       1: [1, 2],              2: [0, 1, 6, 4, 3],     3: [0, 1, 6, 2, 3],
                           4: [5, 6, 1, 2],             5: [0, 5, 6, 2, 3],     6: [0, 5, 6, 2, 3, 4],  7: [0, 1, 2],
                           8: [0, 1, 2, 3, 4, 5, 6],    9: [0, 1, 2, 5, 6]}

    def setTime(self):
        cellsToFill = self.numberList[self.number]
        for num in range(7):
            eval('self.cell' + str(num)).unfill()
        for num in cellsToFill:
            eval('self.cell'+str(num)).fill()


class GUI:

    """ This is the description. """

    def __init__(self):
        self.win = GraphWin('Alarm Clock', 500, 500)
        self.entry = Entry(Point(250, 300), 20)
        self.entry.draw(self.win)
        self.secondTop = Rectangle(Point(245, 145), Point(255, 155))
        self.secondBottom = Rectangle(Point(245, 95), Point(255, 105))
        self.secondTop.setFill('black')
        self.secondTop.draw(self.win)
        self.secondBottom.setFill('black')
        self.secondBottom.draw(self.win)
        self.upHour = Button(self.win, Point(50, 350), 100, 40, '+ HOUR', 'light blue')
        self.downHour = Button(self.win, Point(50, 420), 100, 40, '- HOUR', 'light blue')
        self.upMinute = Button(self.win, Point(200, 350), 100, 40, '+ MINUTE', 'light blue')
        self.downMinute = Button(self.win, Point(200, 420), 100, 40, '- MINUTE', 'light blue')
        self.change = Button(self.win, Point(350, 350), 100, 40, 'CHANGE', 'light blue')
        self.quit = Button(self.win, Point(350, 420), 100, 40, 'QUIT', 'light blue')
        self.buttons = [self.upHour, self.downHour, self.upMinute, self.downMinute, self.change, self.quit]
        for button in self.buttons:
            button.activate()
        self.am = True
        self.amText = Text(Point(430, 250), '')
        self.amText.setSize(24)
        self.amText.draw(self.win)
        self.changeAMPM(self.am)
        self.amInstruction = Text(Point(250, 255), "Click to Change AM / PM")
        self.amInstruction.setSize(8)
        self.amInstruction.draw(self.win)

    def changeAMPM(self, am):
        if am:
            self.amText.setText('AM')
        else:
            self.amText.setText('PM')


def initializeDigits(gui):
    centers = [Point(70, 125), Point(180, 125), Point(320, 125), Point(430, 125)]
    hour1 = Digit(centers[0], gui)
    hour2 = Digit(centers[1], gui)
    minute1 = Digit(centers[2], gui)
    minute2 = Digit(centers[3], gui)
    return hour1, hour2, minute1, minute2


def checkHour(gui, hour1, hour2, am, amChange):
    if hour2.number == 10:
        hour2.number = 0
        hour1.number = 1
    elif hour2.number == 3 and hour1.number == 1:
        hour1.number = 0
        hour2.number = 1
    if hour1.number == 1 and hour2.number == -1:
        hour1.number = 0
        hour2.number = 9
    elif hour1.number == 0 and hour2.number == 0:
        hour1.number = 1
        hour2.number = 2
    if ((hour1.number == 1 and hour2.number == 2) or (hour1.number == 1 and hour2.number == 1)) and amChange:
        am[0] = not am[0]
        gui.changeAMPM(am[0])


def checkMinute(minute1, minute2, hour2, amChange):
    if minute2.number == 10:
        minute2.number = 0
        minute1.number += 1
    if minute1.number == 6:
        hour2.number += 1
        minute1.number = 0
        minute2.number = 0
        amChange = True
    if minute1.number == 0 and minute2.number == -1:
        minute1.number = 5
        minute2.number = 9
        hour2.number += -1
        amChange = True
    elif minute2.number == -1:
        minute1.number += -1
        minute2.number = 9
    return amChange


def takeEntry(str, hour1, hour2, minute1, minute2):
    error = False
    try:
        for ch in str:
            if not (ch.isdigit() or ch == ':'):
                error = True
        if not error:
            numbers = str.split(':')
            if not len(numbers) == 2:
                error = True
            if not (len(numbers[0]) == 1 or len(numbers[0]) == 2) or not(len(numbers[1]) == 2):
                error = True
        hours = numbers[0]
        minutes = numbers[1]
        if not error:
            if minutes[0] == '0':
                minutes = minutes[1]
            if hours[0] == '0':
                hours = hours[1]
        testHours = eval(hours)
        testMins = eval(minutes)
    except:
        error = True
    if not error:
        if eval(hours) < 1 or eval(hours) > 12:
            error = True
        if eval(minutes) < 0 or eval(minutes) > 59:
            error = True
    if not error:
        if len(hours) == 1:
            hour1.number = 0
            hour2.number = eval(hours[0])
        elif len(hours) == 2:
            hour1.number = eval(hours[0])
            hour2.number = eval(hours[1])
        if len(minutes) == 1:
            minute1.number = 0
            minute2.number = eval(minutes[0])
        elif len(minutes) == 2:
            minute1.number = eval(minutes[0])
            minute2.number = eval(minutes[1])
        return True

def main():
    gui = GUI()
    hour1, hour2, minute1, minute2 = initializeDigits(gui)
    hour1.number, hour2.number = 1, 2
    m1 = Point(0, 0)
    am = [True]
    amChange = False
    while not gui.quit.clicked(m1):
        if hour1.number == 1 and hour2.number == 0 or hour1.number == 0 and hour2.number == 1:
            amChange = False
        if gui.upHour.clicked(m1):
            hour2.number += 1
        elif gui.upMinute.clicked(m1):
            minute2.number += 1
            amChange = False
        elif gui.downHour.clicked(m1):
            hour2.number += -1
        elif gui.downMinute.clicked(m1):
            minute2.number += -1
            amChange = False
        elif gui.change.clicked(m1):
            am = [takeEntry(gui.entry.getText(), hour1, hour2, minute1, minute2)]
            gui.entry.setText('')
            gui.changeAMPM(am[0])
            amChange = False
        amChange = checkMinute(minute1, minute2, hour2, amChange)
        checkHour(gui, hour1, hour2, am, amChange)
        amChange = True
        hour1.setTime()
        hour2.setTime()
        minute1.setTime()
        minute2.setTime()
        m1 = gui.win.getMouse()


main()

