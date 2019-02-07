#
#Written by: Luke Shannon
#10/17/18
#
#This program plays blackjack!

#import all of my modules
from graphics import *
from button import *
from random import *
from card import *
    
def main():
    
    #Set up the introduction window which asks for name etc.
    win = GraphWin("Welcome", 1200, 700)
    win.setBackground('light green')

    welcomeText = Text(Point(600,200),"Welcome to Blackjack!")
    welcomeText.setSize(35)
    welcomeText.setStyle('bold')
    welcomeText.setTextColor('red')

    #Draws the same text behind it in black for 3D effect
    shadow = welcomeText.clone()
    shadow.setSize(36)
    shadow.setTextColor('black')
    shadow.draw(win)
    welcomeText.draw(win)

    #Entry box for name
    nameBox = Entry(Point(600,350),20)
    nameBox.setSize(18)
    nameBox.setText("What's your name?")
    nameBox.draw(win)

    #Used the introduction as a place to workshop my suit polygons, so they seem to be printed unnecessarily, but I was using this space to work on them, and then left them for an aesthetic opening.
    #hearts
    heartCenter = Point(450,550)
    hCX = heartCenter.getX()
    hCY = heartCenter.getY()
    hearts = Polygon(Point(hCX,hCY-4),Point(hCX-4,hCY-12),Point(hCX-14,hCY-12),Point(hCX-18,hCY),Point(hCX,hCY+20),Point(hCX+18,hCY),Point(hCX+14,hCY-12),Point(hCX+4,hCY-12))
    hearts.setOutline('red')
    hearts.setFill('red')
    hearts.draw(win)
    #spades
    spadesCenter = Point(550,550)
    sCX = spadesCenter.getX()
    sCY = spadesCenter.getY()
    spades = Polygon(Point(sCX,sCY+4),Point(sCX+4,sCY+12),Point(sCX+14,sCY+12),Point(sCX+18,sCY),Point(sCX,sCY-20),Point(sCX-18,sCY),Point(sCX-14,sCY+12),Point(sCX-4,sCY+12),Point(sCX,sCY),Point(sCX-2,sCY+22),Point(sCX+2,sCY+22))
    spades.setFill('black')
    spades.draw(win)
    #diamonds
    diamondsCenter = Point(650,550)
    dCX = diamondsCenter.getX()
    dCY = diamondsCenter.getY()
    diamonds = Polygon(Point(dCX-15,dCY),Point(dCX,dCY+20),Point(dCX+15,dCY),Point(dCX,dCY-20))
    diamonds.setFill('red')
    diamonds.setOutline('red')
    diamonds.draw(win)
    #clubs
    clubsCenter = Point(750,550)
    cCX = clubsCenter.getX()
    cCY = clubsCenter.getY()
    clubs = Polygon(Point(cCX,cCY),Point(cCX-2,cCY+15),Point(cCX+2,cCY+15),Point(cCX,cCY),Point(cCX-12,cCY+6),Point(cCX-18,cCY),Point(cCX-12,cCY-6),Point(cCX,cCY),Point(cCX-6,cCY-12),Point(cCX,cCY-18),Point(cCX+6,cCY-12),Point(cCX,cCY),Point(cCX+12,cCY-6),Point(cCX+18,cCY),Point(cCX+12,cCY+6),Point(cCX,cCY))
    clubs.setFill('black')
    clubs.draw(win)

    #Creating the start button
    start = Button(win,Point(600,450),100,60,"START",True)
    click = win.getMouse()

    #While loop until the start button is clicked and the name is saved / window closed
    while not start.clicked(click):
        click = win.getMouse()
    name = nameBox.getText()  
    win.close()

    #Creating the blackhjack window
    win = GraphWin("Blackjack!",1100,650)
    win.setBackground('light green')
    #Creating the rectangles with a for loop to save time. The equations for many of the positions of objects in this program are not simplified, but just follow my reasoning for getting the points
    #Where they need to be. In this case, the gap between each card is 50 and the width of each card is 125, so the x value is in these terms multiplied by the number of cards before it.
    for i in range(12):
        if i < 6:
            playerRect = Rectangle(Point(50*(i+1)+i*125,50),Point(50*(i+1)+(i+1)*125,225))
            playerRect.draw(win)
        else:
            #Subtract 6 because otherwise i would multiply to create an x that is not in the window
            i = i-6
            compRect = Rectangle(Point(50*(i+1)+i*125,600),Point(50*(i+1)+(i+1)*125,425))
            compRect.draw(win)

    #Creating all of the buttons and scoreboard and deactivating appropriately
    quitButton = Button(win, Point(1050-66,325), 133, 100, "QUIT", True)
    hitButton = Button(win, Point(50+133-66,325), 133, 100, "HIT", False)
    standButton = Button(win, Point(300,325), 133, 100, "STAND", False)
    againButton = Button(win, Point(559-66,325), 133, 100, "PLAY AGAIN", False)
    scoreRect = Rectangle(Point(609,275), Point(877,375))
    scoreRect.setWidth(2)
    scoreRect.draw(win)

    #Creating the nameplates for each player with a variable number of games won, starting at 0
    playerWon = 0
    playerName = Text(Point(150,25),name+": "+ str(playerWon)+" games won.")
    playerName.setStyle('bold')
    playerName.draw(win)
    dealerWon = 0
    dealerName = Text(Point(150,400),"Dealer: "+str(dealerWon)+" games won.")
    dealerName.setStyle('bold')
    dealerName.draw(win)

    #Preparing for the first round
    startText = Text(Point(750,325),"Click anywhere to deal.")
    startText.draw(win)
    click = win.getMouse()
    startText.undraw()

    #Dealing the initial 2 cards to both the player and the dealer
    dC1 = Card(Point(50+63,650-50-175/2),win,randrange(1,14),randrange(1,5),True)
    #fake card has the question mark
    dCfake = Card(Point(50*2+63*3,600-175/2),win,randrange(1,14),randrange(1,5),False)
    pC1 = Card(Point(50+125/2,50+175/2),win,randrange(1,14),randrange(1,5),True)
    pC2 = Card(Point(50*2+125*3/2,50+175/2),win,randrange(1,14),randrange(1,5),True)
    #Total of cards
    playerTotal = 0
    dealerTotal = 0

    #Determining the number of aces and storing in ace total so we can check if there are any aces in our hand while over 21.
    if pC1.getValue() == 1 and pC2.getValue() == 1:
        aceTotal = 2
    elif pC1.getValue()== 1 or pC2.getValue() == 1:
        aceTotal = 1
    else:
        aceTotal = 0

    #Giving each card its appropriate value (A = 11, Q = 10, J = 10, etc)
    if pC1.getValue() == 1:
        playerTotal += 11
    elif pC1.getValue() > 10:
        playerTotal += 10
    else:
        playerTotal += pC1.getValue()
        
    if pC2.getValue() == 1:
        playerTotal += 11
    elif pC2.getValue() > 10:
        playerTotal += 10
    else:
        playerTotal += pC2.getValue()
    if playerTotal > 21:
        aceTotal += -1
        playerTotal += -10

    #Keeping track of the number of cards and preparing for user input
    pCardNum = 2
    hitButton.activate()
    standButton.activate()

    #Start of the while loop, user can now click buttons to make decisions about their cards, until they choose to quit.
    while not quitButton.clicked(click):
        
        #Determining the number of cards the user still has to draw, and then allowing them to hit. pCardNum = player card number.
        if pCardNum == 6:
            hitButton.deactivate()
            
        if hitButton.clicked(click):
            #Each time the user chooses to hit, add one to their card count and create a card, adding its value to the total.
            if pCardNum == 5:
                pCardNum += 1
                pC6 = Card(Point(50*6+125*11/2,50+175/2),win,randrange(1,14),randrange(1,5),True)
                #Check if its an ace
                if pC6.getValue() == 1:
                    playerTotal += 11
                    aceTotal += 1
                    
                #Check if its a face card
                elif pC6.getValue() > 10:
                    playerTotal += 10
                    
                #Otherwise add the value directly.
                else:
                    playerTotal += pC6.getValue()

                    #Same process, but if the player has 4 cards instead of 5 or 6
            elif pCardNum == 4:
                pCardNum += 1
                pC5 = Card(Point(50*5+125*9/2,50+175/2),win,randrange(1,14),randrange(1,5),True)
                if pC5.getValue() == 1:
                    playerTotal += 11
                    aceTotal += 1
                elif pC5.getValue() > 10:
                    playerTotal += 10
                else:
                    playerTotal += pC5.getValue()

                    #If they have 3 cards
            elif pCardNum == 3:
                pCardNum += 1
                pC4 = Card(Point(50*4+125*7/2,50+175/2),win,randrange(1,14),randrange(1,5),True)
                if pC4.getValue() == 1:
                    playerTotal += 11
                    aceTotal += 1
                elif pC4.getValue() > 10:
                    playerTotal += 10
                else:
                    playerTotal += pC4.getValue()

                    #2 cards (the minimum)
            elif pCardNum == 2:
                pCardNum += 1
                pC3 = Card(Point(50*3+125*5/2,50+175/2),win,randrange(1,14),randrange(1,5),True)
                if pC3.getValue() == 1:
                    playerTotal += 11
                    aceTotal += 1
                elif pC3.getValue() > 10:
                    playerTotal += 10
                else:
                    playerTotal += pC3.getValue()

                    #after they hit, check the value of their cards. If they are over 21 with an unconverted ace, remove one from the ace total and 10 from their overall total, as the 11 becomes 1. If they chose to hit at 21 and got an ace, bust them anyway.
            if playerTotal > 21 and playerTotal != 32:
                if aceTotal > 0:
                    aceTotal += -1
                    playerTotal += -10
                    #Otherwise, bust them, showing a losing message
                else:
                    hitButton.deactivate()
                    standButton.deactivate()
                    gameText = Text(Point(740,325),"You Busted with "+ str(playerTotal))
                    gameText.draw(win)
                    #Redraw and redefine the nameplates to include updated scores
                    dealerName.undraw()
                    dealerWon += 1
                    dealerName = Text(Point(150,400),"Dealer: "+str(dealerWon)+" games won.")
                    dealerName.setStyle('bold')
                    dealerName.draw(win)
                    #activate again button for another round
                    againButton.activate()

              #if they choose to stand
        if standButton.clicked(click):
                #deactivate buttons
            hitButton.deactivate()
            standButton.deactivate()

            #begin the dealer's process
            dealerTotal = 0

            #replace the dealer's unknown card with a visible one
            dC2 = Card(Point(50*2+63*3,600-175/2),win,randrange(1,14),randrange(1,5),True)

            #check for aces
            if dC1.getValue() == 1 and dC2.getValue() == 1:
                daceTotal = 2
            elif dC1.getValue()== 1 or dC2.getValue() == 1:
                daceTotal = 1
            else:
                daceTotal = 0

                #Calculate the dealer's total between both cards, adjusting for aces and face cards
            if dC1.getValue() == 1:
                dealerTotal += 11
            elif dC1.getValue() > 10:
                dealerTotal += 10
            else:
                dealerTotal += dC1.getValue()
                
            if dC2.getValue() == 1:
                dealerTotal += 11
            elif dC2.getValue() > 10:
                dealerTotal += 10
            else:
                dealerTotal += dC2.getValue()
            if dealerTotal > 21:
                daceTotal += -1
                dealerTotal += -10

            #if the dealer's total is less than 17, then they must hit
            if dealerTotal < 17:
                #give a card and add its appropriate value / check for aces
                dC3 = Card(Point(50*3+63*5,600-175/2),win,randrange(1,14),randrange(1,5),True)
                if dC3.getValue() == 1:
                    dealerTotal += 11
                    daceTotal += 1
                elif dC3.getValue() > 10:
                    dealerTotal += 10
                else:
                    dealerTotal += dC3.getValue()

                    #if they are over 21 with unchanged aces, turn the ace into a 1
                if dealerTotal > 21 and daceTotal > 0:
                    daceTotal += -1
                    dealerTotal += -10

                    #if they are still below 17, they hit again.
                if dealerTotal < 17:
                    dC4 = Card(Point(50*4+63*7,600-175/2),win,randrange(1,14),randrange(1,5),True)
                    #add to total, check for aces
                    if dC4.getValue() == 1:
                        dealerTotal += 11
                        daceTotal += 1
                    elif dC4.getValue() > 10:
                        dealerTotal += 10
                    else:
                        dealerTotal += dC4.getValue()
                    if dealerTotal > 21 and daceTotal > 0:
                        daceTotal += -1
                        dealerTotal += -10

                        #hit again if under 17, add values and check for aces if busted
                    if dealerTotal < 17:
                        dC5 = Card(Point(50*5+63*9,600-175/2),win,randrange(1,14),randrange(1,5),True)
                        if dC5.getValue() == 1:
                            dealerTotal += 11
                            daceTotal += 1
                        elif dC5.getValue() > 10:
                            dealerTotal += 10
                        else:
                            dealerTotal += dC5.getValue()
                        if dealerTotal > 21 and daceTotal > 0:
                            daceTotal += -1
                            dealerTotal += -10

                            #final hit if still somehow under 17
                        if dealerTotal < 17:
                            dC6 = Card(Point(50*6+63*11,600-175/2),win,randrange(1,14),randrange(1,5),True)
                            if dC6.getValue() == 1:
                                dealerTotal += 11
                                daceTotal += 1
                            elif dC6.getValue() > 10:
                                dealerTotal += 10
                            else:
                                dealerTotal += dC6.getValue()
                #if the dealer busted and was unable to convert an ace, tell the player they won and change the scoreboard, activate play again button
            if dealerTotal > 21:
                gameText = Text(Point(740,325),"Dealer Busted with "+ str(dealerTotal))
                gameText.draw(win)
                playerName.undraw()
                playerWon += 1
                playerName = Text(Point(150,25),name+": "+ str(playerWon)+" games won.")
                playerName.setStyle('bold')
                playerName.draw(win)
                againButton.activate()
                
                #if the dealer did not bust and has a greater value than what the player stood at, tell the player the dealer won and adjust score and activate again button
            elif dealerTotal > playerTotal:
                gameText = Text(Point(740,325),"Dealer Won: "+ str(dealerTotal)+" > "+str(playerTotal))
                gameText.draw(win)
                dealerName.undraw()
                dealerWon += 1
                dealerName = Text(Point(150,400),"Dealer: "+str(dealerWon)+" games won.")
                dealerName.setStyle('bold')
                dealerName.draw(win)
                againButton.activate()
                
                #If the dealer and player tied, tell the player and activate again button
            elif dealerTotal == playerTotal:
                gameText = Text(Point(740,325),"It's a Push: "+ str(dealerTotal)+" = "+str(playerTotal))
                gameText.draw(win)
                againButton.activate()

                #if the dealer lost to the player, tell the player and change the scoreboard, activate play again
            elif dealerTotal < playerTotal:
                gameText = Text(Point(740,325),str(name)+" Won: "+ str(playerTotal)+" > "+str(dealerTotal))
                gameText.draw(win)
                playerName.undraw()
                playerWon += 1
                playerName = Text(Point(150,25),name+": "+ str(playerWon)+" games won.")
                playerName.setStyle('bold')
                playerName.draw(win)
                againButton.activate()
                #catch any errors just in case, as the statements above should cover every possible situation
            else:
                print("I'm confused.")

                #after determining who won, prepare for the possibility of playing again
        if againButton.clicked(click):
                #reset the board by clearing game text and redrawing rectangles to cover the old cards, as we did initially
            gameText.undraw()
            for i in range(12):
                if i < 6:
                    playerRect = Rectangle(Point(50*(i+1)+i*125,50),Point(50*(i+1)+(i+1)*125,225))
                    playerRect.setFill('light green')
                    playerRect.draw(win)
                else:
                    i = i-6
                    compRect = Rectangle(Point(50*(i+1)+i*125,600),Point(50*(i+1)+(i+1)*125,425))
                    compRect.setFill('light green')
                    compRect.draw(win)

                    #redeal the two initial cards and reset totals, just as before the while loop
            dC1 = Card(Point(50+63,650-50-175/2),win,randrange(1,14),randrange(1,5),True)
            dCfake = Card(Point(50*2+63*3,600-175/2),win,randrange(1,14),randrange(1,5),False)
            pC1 = Card(Point(50+125/2,50+175/2),win,randrange(1,14),randrange(1,5),True)
            pC2 = Card(Point(50*2+125*3/2,50+175/2),win,randrange(1,14),randrange(1,5),True)
            playerTotal = 0
            dealerTotal = 0

                #calculate the values of the player's hand and number of aces, as before the while loop
            if pC1.getValue() == 1 and pC2.getValue() == 1:
                aceTotal = 2
            elif pC1.getValue()== 1 or pC2.getValue() == 1:
                aceTotal = 1
            else:
                aceTotal = 0
                
            if pC1.getValue() == 1:
                playerTotal += 11
            elif pC1.getValue() > 10:
                playerTotal += 10
            else:
                playerTotal += pC1.getValue()
                
            if pC2.getValue() == 1:
                playerTotal += 11
            elif pC2.getValue() > 10:
                playerTotal += 10
            else:
                playerTotal += pC2.getValue()
            if playerTotal > 21:
                aceTotal += -1
                playerTotal += -10

            pCardNum = 2

            #fix buttons for user input
            hitButton.activate()
            standButton.activate()
            againButton.deactivate()
            
            #continue asking for clicks in the while loop so that the user can always input
        click = win.getMouse()

    #close the window once the quit button is clicked
    win.close()














                   
