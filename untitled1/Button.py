from graphics import *
class Button:

    def __init__(self, win, corner, width, height, label, color):
        self.win = win
        self.corner = corner
        self.width = width
        self.height = height
        self.label = label
        self.color = color

        self.xmin = corner.getX()
        self.ymin = corner.getY()
        self.xmax = corner.getX() + width #bottom left corner to place button
        self.ymax = corner.getY() + height
        
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)

        self.rect = Rectangle(p1,p2)
        self.rect.draw(win)

        self.buttonText = Text(Point(self.xmin + 0.5*self.width, self.ymin + 0.5*self.height), self.label)
        self.buttonText.draw(self.win)
        
        self.deactivate()

    def deactivate(self):
        self.active = False
        self.buttonText.setFill("grey")
        self.rect.setFill("light grey")
        self.rect.setOutline("light grey")
        self.rect.setWidth(1)
             
    def activate(self):
        self.active = True
        self.buttonText.setFill("black")
        self.buttonText.setStyle("bold")
        self.rect.setFill(self.color)
        self.rect.setOutline("black")
        self.rect.setWidth(2)

    def clicked(self, point):
        wasClicked = False
        if self.xmin <= point.getX() <= self.xmax:
            if self.ymin <= point.getY() <= self.ymax:
                if self.active:
                    wasClicked = True
        return wasClicked

    def undrawButton(self):
        self.buttonText.undraw()
        self.rect.undraw()

    def setLabel(self, newLabel):
        self.buttonText.setText(newLabel)
