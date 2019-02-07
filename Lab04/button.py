#
#Written by: Luke Shannon
#10/02/18
#
#This program creates a button module to be used in later labs.

from graphics import *

class Button:
    
    """__init__(win, center, width, height, label, activate)
    activate()
    deactivate()
    clicked() [only if active]
    getLabel()
    setLabel()"""

#CONSTRUCTOR
    def __init__(self, win, center, width, height, label, activate):
#Defining outline of button to determine later if it was clicked inside.
        self.xmin = center.getX()-width/2
        self.xmax = center.getX()+width/2
        self.ymin = center.getY()-height/2
        self.ymax = center.getY()+height/2

        p1 = Point(self.xmin,self.ymin)
        p2 = Point(self.xmax,self.ymax)

        self.outline = Rectangle(p1,p2)
        self.outline.draw(win)

        self.label = Text(center, label)
        self.label.draw(win)
#activate or deactivate depending on initials
        if activate:
            self.activate()
            
        else:
            self.deactivate()
        
    def activate(self):
        'Sets this button to active'
        self.active = True
        #Change thickness and color so it looks active
        self.label.setFill("black")
        self.outline.setWidth(2)

    def deactivate(self):
        'sets this button to inactive'
        self.active = False
        #Change thickness and color so it looks inactive
        self.label.setFill("grey")
        self.outline.setWidth(1)

    def clicked(self, point):
        'checks if the button was clicked'
        wasClicked = False
        if self.xmin <= point.getX() <= self.xmax:
            if self.ymin <= point.getY() <= self.ymax:
                if self.active:
                    wasClicked = True
        return wasClicked

    def getLabel(self):
        return self.label

    def setLabel(self, newlabel):
        self.label = newlabel

    
