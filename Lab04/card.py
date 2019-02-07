#
#Written by: Luke Shannon
#10/09/18
#350x250
#This module creates playing cards

from graphics import *
from random import *

class Card:

    """__init__(self, center, win, rank, suit, real)
    takes numbers 1-4 as suit
    takes numbers 1-13 as rank
    getValue() returns rank"""

    def __init__(self, center, win, rank, suit, real):
        self.rank = rank
        self.suit = suit
        self.win = win
        self.centerX = center.getX()
        self.centerY = center.getY()
        #Getting the outline of the card size to fill later
        cardBack = Rectangle(Point(self.centerX-125/2,self.centerY-175/2),Point(self.centerX+125/2,self.centerY+175/2))
        cardBack.setWidth(2)
    #clubs -- some repetition here, but not problematic. Determines the suit and gives a value to the card
    #So that they can be drawn later
        if self.suit == 1:
            color = 'black'
            if self.rank > 10:
                if self.rank == 11:
                    value = 'J'
                elif self.rank == 12:
                    value = 'Q'
                elif self.rank == 13:
                    value = 'K'
                else:
                    value = 'error'
            elif self.rank == 1:
                value = 'A'
            else:
                value = self.rank
    #diamonds -- see comment above
        if self.suit == 2:
            color = 'red'
            if self.rank > 10:
                if self.rank == 11:
                    value = 'J'
                elif self.rank == 12:
                    value = 'Q'
                elif self.rank == 13:
                    value = 'K'
                else:
                    self.value = 'errpr'
            elif self.rank == 1:
                value = 'A'
            else:
                value = self.rank
    #hearts -- see comment above
        if self.suit == 3:
            color = 'red'
            if self.rank > 10:
                if self.rank == 11:
                    value = 'J'
                elif self.rank == 12:
                    value = 'Q'
                elif self.rank == 13:
                    value = 'K'
                else:
                    value = 'errpr'
            elif self.rank == 1:
                value = 'A'
            else:
                value = self.rank
    #spades -- see comment above
        if self.suit == 4:
            color = 'black'
            if self.rank > 10:
                if self.rank == 11:
                    value = 'J'
                elif self.rank == 12:
                    value = 'Q'
                elif self.rank == 13:
                    value = 'K'
                else:
                    value = 'errpr'
            elif self.rank == 1:
                value = 'A'
            else:
                value = self.rank

        #Draw a blank card with a question mark for when the card is not yet revealed
        if not real:
            cardBack.setFill('white')
            cardBack.draw(self.win)
            fakeText = Text(Point(self.centerX,self.centerY),"?")
            fakeText.setSize(36)
            fakeText.draw(win)

        #Drawing the card and with both the rank and suit
        else:
            #card back
            cardBack.setFill('white')
            cardBack.draw(self.win)

            #Rank Text with the appropriate color and size
            valueText = Text(Point(self.centerX-25,self.centerY),str(value))
            valueText.setFill(color)
            valueText.setSize(36)
            valueText.draw(self.win)

            #Preparing all types of suits to be drawn, all at the same point, so that we can decide later which to choose
            heartCenter = Point(self.centerX+25,self.centerY)
            hCX = heartCenter.getX()
            hCY = heartCenter.getY()
            hearts = Polygon(Point(hCX,hCY-4),Point(hCX-4,hCY-12),Point(hCX-14,hCY-12),Point(hCX-18,hCY),Point(hCX,hCY+20),Point(hCX+18,hCY),Point(hCX+14,hCY-12),Point(hCX+4,hCY-12))
            hearts.setOutline('red')
            hearts.setFill('red')
    
            spadesCenter = Point(self.centerX+25,self.centerY)
            sCX = spadesCenter.getX()
            sCY = spadesCenter.getY()
            spades = Polygon(Point(sCX,sCY+4),Point(sCX+4,sCY+12),Point(sCX+14,sCY+12),Point(sCX+18,sCY),Point(sCX,sCY-20),Point(sCX-18,sCY),Point(sCX-14,sCY+12),Point(sCX-4,sCY+12),Point(sCX,sCY),Point(sCX-2,sCY+22),Point(sCX+2,sCY+22))
            spades.setFill('black')
      
            diamondsCenter = Point(self.centerX+25,self.centerY)
            dCX = diamondsCenter.getX()
            dCY = diamondsCenter.getY()
            diamonds = Polygon(Point(dCX-15,dCY),Point(dCX,dCY+20),Point(dCX+15,dCY),Point(dCX,dCY-20))
            diamonds.setFill('red')
            diamonds.setOutline('red')
            
            clubsCenter = Point(self.centerX+25,self.centerY)
            cCX = clubsCenter.getX()
            cCY = clubsCenter.getY()
            clubs = Polygon(Point(cCX,cCY),Point(cCX-2,cCY+15),Point(cCX+2,cCY+15),Point(cCX,cCY),Point(cCX-12,cCY+6),Point(cCX-18,cCY),Point(cCX-12,cCY-6),Point(cCX,cCY),Point(cCX-6,cCY-12),Point(cCX,cCY-18),Point(cCX+6,cCY-12),Point(cCX,cCY),Point(cCX+12,cCY-6),Point(cCX+18,cCY),Point(cCX+12,cCY+6),Point(cCX,cCY))
            clubs.setFill('black')

          #Depending on the randomly generated number 1-4, draw the appropriate suit (alphabetically)
            if self.suit == 1:
                clubs.draw(win)
            elif self.suit == 2:
                diamonds.draw(win)
            elif self.suit == 3:
                hearts.draw(win)
            elif self.suit == 4:
                spades.draw(win)
            else:
                print("sad error")

    #Get Value function necessary for after drawing and randomizing the card, so I can input randrange directly into my constructor, but still access the values later.
    def getValue(self):
        return self.rank
















            
    
        
