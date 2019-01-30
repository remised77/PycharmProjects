#
# Written by: Luke Shannon
# 11/27/18
#
# This program runs the shark game!

from fish import *
from shark import *
from sharkGUI import *


def main():
    # Begin with one large try function, as to prevent any red from ever appearing, especially when the window is closed unexpectedly.
    try:
        again = True
        # Set up the window by initializing sharkGUI.
        gui = sharkGUI()
        while again:
            # These variables will be called later to determine if the game has ended.
            gameOver = False
            stalemate = False
            again = False
            # Make sure to only restart the screen after the replay button
            gui.setUp()
            # We cannot return the initial placements of the fish through an __init__, so gui.getInitials() returns those now.
            initials = gui.getInitials()
            fish1P, fish2P, fish3P, fish1D, fish2D, fish3D = initials[0], initials[1], initials[2], initials[3], initials[4], initials[5]
            # The shark always starts at Point(7,2), and is initialized as such.
            sharkP = Point(7, 2)
            sharkObj = shark(sharkP, fish1P, fish2P, fish3P)
            # The fish are initialized according to the values returned by guiInitials() earlier.
            fish1 = fish(fish1P, fish1D)
            fish2 = fish(fish2P, fish2D)
            fish3 = fish(fish3P, fish3D)
            fishCount = 3
            # The turns counter will tell us if it is the fish or shark turn to move, or if the game has gone on too long.
            turns = 0
            # User click to start the game, repeating until they click start or quit.
            m1 = gui.getClick()
            while not gui.checkMoveClicked(m1) and not gui.checkQuitClicked(m1): m1 = gui.getClick()
            # Main loop. Continue to run unless the user clicks quit.
            while not gui.checkQuitClicked(m1):
                turns += 1
                # If the move button is clicked on an odd turn, then the fish must move.
                if gui.checkMoveClicked(m1) and turns % 2 == 1:
                    # This set of functions calls gui to draw the fish according to the fish's number, position, flee mode, and direction.
                    # While simultaneously calling the fish to move (fishX.move).
                    gui.fleeDirect(1, fish1.move(sharkObj.returnShark(), fish2.returnPoint(), fish3.returnPoint()), fish1.returnFlee(), fish1.returnDirection())
                    gui.fleeDirect(2, fish2.move(sharkObj.returnShark(), fish1.returnPoint(), fish3.returnPoint()), fish2.returnFlee(), fish2.returnDirection())
                    gui.fleeDirect(3, fish3.move(sharkObj.returnShark(), fish1.returnPoint(), fish2.returnPoint()), fish3.returnFlee(), fish3.returnDirection())
                    # And the button label changes to "Move Shark".
                    gui.changeLabelShark()
                # If the move button is clicked on an even turn, then the shark moves.
                if gui.checkMoveClicked(m1) and turns % 2 == 0:
                    # This function moves the shark according to the locations of the three fish.
                    sharkObj.getShark(fish1.returnPoint(), fish2.returnPoint(), fish3.returnPoint())
                    # Which is then drawn into the screen.
                    gui.drawShark(sharkObj.returnShark())
                    # And the button label is changed to "Move Fish".
                    gui.changeLabelFish()
                # These values are created to check if the shark has eaten any fish.
                allFish = [fish1, fish2, fish3]
                #draw white rectangle so info is cleared
                gui.clearMessage()
                for i in range(3):
                    # If the x and y values of the shark are equal to the x and y values of any fish, then...
                    if sharkObj.returnShark().getX() == allFish[i].returnPoint().getX() and sharkObj.returnShark().getY() == allFish[i].returnPoint().getY():
                        # Set that fish as eaten (and move it away).
                        allFish[i].setEaten(True)
                        # Tell user a fish has been eaten.
                        gui.setMessage("Fish " + str(i+1) + " has been eaten.")
                        # And update the fishCount (one fewer).
                        fishCount += -1
                    # And redraw the fish so that any eaten fish disappear.
                    gui.fleeDirect(i, allFish[i].returnPoint(), allFish[i].returnFlee(), allFish[i].returnDirection())
                # If there is only one fish left, then it is possible that the game is in a stalemate.
                if fishCount == 1:
                    for i in range(3):
                        # A stalemate occurs when a fish is repeatedly able to escape through a wall. When there is one fish left on the same row as the shark,
                        # the chase begins. During a chase that results in a stalemate, there is always a point where the fish is 8 spaces from the shark, on its row, and facing the shark.
                        xDist = allFish[i].returnPoint().getX() - sharkObj.returnShark().getX()
                        yDist = allFish[i].returnPoint().getY() - sharkObj.returnShark().getY()
                        # If the distance is 8, and the fish is moving towards the shark, then a stalemate has occurred,
                        # or too many turns have occurred (in case of an unforeseen stalemate situation).
                        if (yDist == 0 and ((xDist == 8 and allFish[i].returnDirection() == 3) or (xDist == -8 and allFish[i].returnDirection() == 1))) or turns == 55:
                            stalemate = True
                            gameOver = True
                        # Repeated as above.
                        elif xDist == 0 and ((yDist == 8 and allFish[i].returnDirection() == 0) or (yDist == -8 and allFish[i].returnDirection() == 2)):
                            stalemate = True
                            gameOver = True
                        else:
                            None
                # The game also ends if all the fish are eaten.
                elif fishCount == 0:
                    gameOver = True
                    stalemate = False
                else:
                    None
                # If there is a stalemate, break the loop.
                if stalemate or gameOver:
                    break
                # Otherwise, continue asking for inputs.
                m1 = gui.getClick()
        # If the user has not pressed quit, then tell them why the game is over (fishGone), and ask if they want to continue.
            if gameOver and gui.fishGone(stalemate):
                # If they play again, run the program again!
                gui.clearMessage()
                again = True
    except:
        None


main()
