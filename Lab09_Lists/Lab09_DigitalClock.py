#
# Written by: Luke Shannon
# 01/29/19
# This program creates a digital clock.

from Lab09_Button import *
from Lab09_graphics import *


class Cell:

    """ This class creates the cell of a digit and controls whether each cell is filled or unfilled. """

    def __init__(self, gui, center, orientation='x'):
        # The orientation of the cell is defaulted to the x direction unless otherwise stated.
        # gui is passed here and in many locations so that the draw methods can be accessed inside other classes.
        self.gui = gui
        self.win = gui.win
        self.center = center
        self.orientation = orientation
        x = self.center.getX()
        y = self.center.getY()
        # Draws the polygon of the cell.
        if self.orientation:
            self.cell = Polygon(Point(x+45, y), Point(x+40, y+5), Point(x-40, y+5),
                                Point(x-45, y), Point(x-40, y-5), Point(x+40, y-5))
        else:
            self.cell = Polygon(Point(x, y-45), Point(x+5, y-40), Point(x+5, y+40),
                                Point(x, y+45), Point(x-5, y+40), Point(x-5, y-40))
        self.cell.setFill('white')
        self.cell.draw(self.win)

    def fill(self):
        # This function fills the cell.
        self.cell.setFill('black')

    def unfill(self):
        # This function unfills the cell.
        self.cell.setFill('white')
        self.cell.setOutline('white')


class Digit:

    """ This class controls a digit for the clock, and uses the cell
    class in order to create and control its sub-cells. """

    def __init__(self, center, gui):
        self.gui = gui
        self.center = center
        self.number = 0

        # Initialize the cells for the digit around the center with which the digit class is initialized.
        self.cell0 = Cell(self.gui, Point(center.getX(), center.getY() - 90))
        self.cell1 = Cell(self.gui, Point(center.getX() + 45, center.getY() - 45), False)
        self.cell2 = Cell(self.gui, Point(center.getX() + 45, center.getY() + 45), False)
        self.cell3 = Cell(self.gui, Point(center.getX(), center.getY() + 90))
        self.cell4 = Cell(self.gui, Point(center.getX() - 45, center.getY() + 45), False)
        self.cell5 = Cell(self.gui, Point(center.getX() - 45, center.getY() - 45), False)
        self.cell6 = Cell(self.gui, Point(center.getX(), center.getY()))

        # The numberList is a dictionary which takes in a key of the number that the digit class should show, and
        # outputs the numbers of the cells that should be filled in order to display that number.
        self.numberList = {0: [0, 1, 2, 3, 4, 5],       1: [1, 2],              2: [0, 1, 6, 4, 3],     3: [0, 1, 6, 2, 3],
                           4: [5, 6, 1, 2],             5: [0, 5, 6, 2, 3],     6: [0, 5, 6, 2, 3, 4],  7: [0, 1, 2],
                           8: [0, 1, 2, 3, 4, 5, 6],    9: [0, 1, 2, 5, 6]}

    def setTime(self):
        # This method fills the cells of the digit class according to the number that the numberList provides.
        cellsToFill = self.numberList[self.number]
        # First we unfill every cell.
        for num in range(7):
            eval('self.cell' + str(num)).unfill()
        # And then fill the relevant ones.
        for num in cellsToFill:
            eval('self.cell'+str(num)).fill()


class GUI:

    """ This class controls the gui interface of the program in order to be more easily accessed through different
     classes, and easily draw all of the start the initial state of the clock."""

    def __init__(self):
        # Create the window, entry, and second colon.
        self.win = GraphWin('Alarm Clock', 500, 500)
        self.entry = Entry(Point(250, 300), 20)
        self.entry.draw(self.win)
        self.secondTop = Rectangle(Point(245, 145), Point(255, 155))
        self.secondBottom = Rectangle(Point(245, 95), Point(255, 105))
        self.secondTop.setFill('black')
        self.secondTop.draw(self.win)
        self.secondBottom.setFill('black')
        self.secondBottom.draw(self.win)
        # Create the buttons using the button class
        self.upHour = Button(self.win, Point(50, 350), 100, 40, '+ HOUR', 'light blue')
        self.downHour = Button(self.win, Point(50, 420), 100, 40, '- HOUR', 'light blue')
        self.upMinute = Button(self.win, Point(200, 350), 100, 40, '+ MINUTE', 'light blue')
        self.downMinute = Button(self.win, Point(200, 420), 100, 40, '- MINUTE', 'light blue')
        self.change = Button(self.win, Point(350, 350), 100, 40, 'CHANGE', 'light blue')
        self.quit = Button(self.win, Point(350, 420), 100, 40, 'QUIT', 'light blue')
        # Activate the buttons.
        self.buttons = [self.upHour, self.downHour, self.upMinute, self.downMinute, self.change, self.quit]
        for button in self.buttons:
            button.activate()
        # Sets up am/pm and draws am to the window.
        self.am = True
        self.amText = Text(Point(430, 250), '')
        self.amText.setSize(24)
        self.amText.draw(self.win)
        self.changeAMPM(self.am)
        # Initial instructions which allow the user to click to change AM / PM while the clock is at 12 or 11, as that
        # is the state of the clock when the program starts.
        self.amInstruction = Text(Point(250, 255), "Click to Change AM / PM")
        self.amInstruction.setSize(8)
        self.amInstruction.draw(self.win)

    def changeAMPM(self, am):
        # This function changes the am / pm sign on the screen.
        if am:
            self.amText.setText('AM')
        else:
            self.amText.setText('PM')


def initializeDigits(gui):
    # This function initializes the digits and their centers for the program.
    centers = [Point(70, 125), Point(180, 125), Point(320, 125), Point(430, 125)]
    hour1 = Digit(centers[0], gui)
    hour2 = Digit(centers[1], gui)
    minute1 = Digit(centers[2], gui)
    minute2 = Digit(centers[3], gui)
    return hour1, hour2, minute1, minute2


def checkHour(gui, hour1, hour2, am, amChange):
    # This function checks if the hour numbers are feasible and adjusts them if they are not
    # If the hour number is 10, then the time should be 10 o'clock.
    if hour2.number == 10:
        hour2.number = 0
        hour1.number = 1
    # If the second digit is three and the first digit is 1 then the time should be 1 o'clock.
    elif hour2.number == 3 and hour1.number == 1:
        hour1.number = 0
        hour2.number = 1
    # If the first digit is 1 and the second digit is -1 then the time should be 9 o'clock.
    if hour1.number == 1 and hour2.number == -1:
        hour1.number = 0
        hour2.number = 9
    # If both digits are 0 then the time should be 12 o'clock.
    elif hour1.number == 0 and hour2.number == 0:
        hour1.number = 1
        hour2.number = 2
    # If the hour was changed (amChange) and now the time is 12 or 11 then am / pm should also change.
    if ((hour1.number == 1 and hour2.number == 2) or (hour1.number == 1 and hour2.number == 1)) and amChange:
        am[0] = not am[0]
        gui.changeAMPM(am[0])


def checkMinute(minute1, minute2, hour1, hour2, amChange):
    # This function checks the minutes are feasible and then adjusts them if they are not.
    # If the second minute digit is 10 then the first digit should be increased by 1 and the second reset to 0.
    if minute2.number == 10:
        minute2.number = 0
        minute1.number += 1
    # If the first digit is 6 then the hour should increase and the second should not, and the computer should
    # check for amChange
    if minute1.number == 6:
        minute1.number = 0
        minute2.number = 0
    # If the hour is 10 then the am / pm should not change as a result of a minute change.
        if not(hour1.number == 1 and hour2.number == 0):
            amChange = True
        hour2.number += 1
    # If the minutes are less than 0 then the hour should reduce by 1.
    if minute1.number == 0 and minute2.number == -1:
        minute1.number = 5
        minute2.number = 9
    # If the hour is currently 10 or 1, then the am/pm should not change as a result of the minute change
        if not(hour1.number == 1 and (hour2.number == 0 or hour2.number == 1) or hour1.number == 0 and hour2.number == 1):
            amChange = True
        hour2.number += -1
    # if only the second minute digit is less than 0 then the first minute digit should be reduced by 1.
    elif minute2.number == -1:
        minute1.number += -1
        minute2.number = 9
    return amChange


def takeEntry(str, hour1, hour2, minute1, minute2):
    # This function takes an entry and checks if it is a valid input, and then adjusts the time accordingly.
    error = False
    try:
        # If any character is not a digit or a colon, then the time is not valid.
        for ch in str:
            if not (ch.isdigit() or ch == ':'):
                error = True
        # If the string cannot be split into a list of length 2, then the input is not valid.
        if not error:
            numbers = str.split(':')
            if not len(numbers) == 2:
                error = True
                # If the number of hours digits is not equal to 1 or 2 or the minutes digits are not equal to 2, then
                # the input is not valid.
            if not (len(numbers[0]) == 1 or len(numbers[0]) == 2) or not(len(numbers[1]) == 2):
                error = True
        hours = numbers[0]
        minutes = numbers[1]
        # If either of the first digits places for minutes or hours is a 0, then replace it with nothing.
        if not error:
            if minutes[0] == '0':
                minutes = minutes[1]
            if hours[0] == '0':
                hours = hours[1]
        # If the hours and minutes cannot be evaluated by eval() ('01'), then the input is invalid.
        testHours = eval(hours)
        testMins = eval(minutes)
    except:
        error = True
    # If the hours are not between 1 and 12 or the minutes are not between 0 and 60, then the input is invalid.
    if not error:
        if eval(hours) < 1 or eval(hours) > 12:
            error = True
        if eval(minutes) < 0 or eval(minutes) > 59:
            error = True
    # If the input is still valid at this point, then set the hour and minute numbers equal to this input.
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
    # This is the main function.
    # Initialize the digit, cell, gui classes, and set the initial states (AM, 12 o'clock) for the clock.
    gui = GUI()
    hour1, hour2, minute1, minute2 = initializeDigits(gui)
    hour1.number, hour2.number = 1, 2
    m1 = Point(0, 0)
    am = [True]
    amChange = False
    while not gui.quit.clicked(m1):
        # If the hour is 1 or 10, then an hour change should not trigger an AM / PM increase.
        if hour1.number == 1 and hour2.number == 0 or hour1.number == 0 and hour2.number == 1:
            amChange = False
        # If a button on the gui is clicked, perform the appropriate action.
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
            # If the entry change is clicked, then take the entry and set the text to 0.
            am = [takeEntry(gui.entry.getText(), hour1, hour2, minute1, minute2)]
            gui.entry.setText('')
            gui.changeAMPM(am[0])
            amChange = False
        # Check if the AM / PM needs to be changed, and perform the hourCheck and minuteCheck.
        amChange = checkMinute(minute1, minute2, hour1, hour2, amChange)
        checkHour(gui, hour1, hour2, am, amChange)
        amChange = True
        # Set the time of the clock according to the new values of the hours and minutes.
        hour1.setTime()
        hour2.setTime()
        minute1.setTime()
        minute2.setTime()
        # Get the user mouseclick.
        m1 = gui.win.getMouse()
        # Undraw the initial description (repeated undraws do not affect the program).
        gui.amInstruction.undraw()


main()

