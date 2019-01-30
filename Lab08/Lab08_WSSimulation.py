#
# Written By: Luke Shannon
# 01/20/19
# Welcome to the simulation.

from WSPlayer import *


class Output:

    '''d'''

    def __init__(self):
        self.playbyplayfile = open('WSplaybyplay.py', 'w')
        self.simulationsfile = open('WSsimulations.py', 'w')

    def simulations(self, simulations):
        self.simulations = simulations

    def closeFiles(self):
        self.playbyplayfile.close()
        self.simulationsfile.close()

    def writeIntros(self):
        if self.simulations == 1:
            print("\nResults of World Series Simulation:\n")
            print("Dodgers-Red Sox World Series Simulation:", file=self.playbyplayfile)
        else:
            print("\nResults of " + str(self.simulations) + " World Series Simulations:\n")
            print("Dodgers-Red Sox World Series Simulation\n", file=self.simulationsfile)


    def writePlay(self, hitter, hit):
        type = [' was out', ' singled', ' doubled', ' tripled', ' homered']
        print('\n' + hitter + type[hit], end='', file=self.playbyplayfile)

    def writeScorers(self, scorer):
        if scorer:
            print(" (" + scorer + " scored)", end = '', file=self.playbyplayfile)
        else:
            None

    def inningName(self, name, number):
        print("\n\nInning "+str(number)+' - '+str(name), file=self.playbyplayfile)

    def writeScore(self, redSoxRuns, dodgerRuns):
        print('\n\nScore: Red Sox {} - Dodgers {}'.format(redSoxRuns, dodgerRuns), end = '', file=self.playbyplayfile)

    def writeGames(self, number):
        print("\n\n========== Game " + str(number) + " ==========", file=self.playbyplayfile)

    def writeSeries(self, series, winner, games):
        print(str(series) + ': ' + str(winner) + ' win in ' + str(games), file=self.simulationsfile)








class Inning:

    '''d'''

    def __init__(self, lineup, team, output, simulations):
        self.outs = 0
        self.spot = 0
        self.bases = [0, 0, 0, 0, 0, 0, 0]
        self.runs = 0
        self.number = 0
        self.lineup = lineup
        self.team = team
        self.output = output
        self.simulations = simulations

    def playOne(self):
        while self.outs < 3:
            if self.spot > 8:
                self.spot = 0
            hit = self.lineup[self.spot].swing()
            self.baseHit(hit)
            self.spot += 1
        self.resetInning()
        self.number += 1

        # if there are less than 3 outs, play an at bat
        # cycle lineup
        # keep going until 3 outs

    def baseHit(self, swing):
        hitter = self.lineup[self.spot].name
        if self.simulations == 1:
            self.output.writePlay(hitter, swing)
        if swing:
            for i in [2, 1, 0]:
                if self.bases[i]:
                    self.bases[i+swing] = self.bases[i]
                    self.bases[i] = 0
            self.bases[swing-1] = hitter
        else:
            self.outs += 1
        for i in range(3, 7):
            if self.bases[i]:
                scorer = self.bases[i]
                if self.simulations == 1:
                    self.output.writeScorers(scorer)
                self.bases[i] = 0
                self.runs += 1

    def resetInning(self):
        self.outs = 0
        self.bases = [0, 0, 0, 0, 0, 0, 0]

    def resetGame(self):
        self.outs = 0
        self.bases = [0, 0, 0, 0, 0, 0, 0]
        self.runs = 0
        self.number = 0
        self.spot = 0

def inputs():
    print("\nWelcome to the World Series!\n")
    simulations = eval(input("How many games would you like to simulate? "))
    return simulations

def create_players(redSox, dodgers):
    infileR = open('Redsox.tsv', 'r')
    textRedSox = infileR.read()
    lines = textRedSox.split('\n')
    player0R = Player(lines[0], 0)
    player1R = Player(lines[1], 1)
    player2R = Player(lines[2], 2)
    player3R = Player(lines[3], 3)
    player4R = Player(lines[4], 4)
    player5R = Player(lines[5], 5)
    player6R = Player(lines[6], 6)
    player7R = Player(lines[7], 7)
    player8R = Player(lines[8], 8)
    # redSox[0], redSox[1], redSox[2], redSox[3], redSox[4], redSox[5], redSox[6], redSox[7], redSox[8] = player0R, player1R, player2R, player3R, player4R, player5R, player6R, player7R, player8R
    for i in range(9):
        redSox.append(eval('player'+str(i)+'R'))
    infileR.close()

    infileD = open('Dodgers.tsv', 'r')
    textDodgers = infileD.read()
    lines = textDodgers.split('\n')
    player0D = Player(lines[0], 0)
    player1D = Player(lines[1], 1)
    player2D = Player(lines[2], 2)
    player3D = Player(lines[3], 3)
    player4D = Player(lines[4], 4)
    player5D = Player(lines[5], 5)
    player6D = Player(lines[6], 6)
    player7D = Player(lines[7], 7)
    player8D = Player(lines[8], 8)
    for i in range(9):
        dodgers.append(eval('player'+str(i)+'D'))
    infileD.close()

def main():

    simulations = inputs()
    redSox = []
    dodgers = []
    output = Output()
    output.simulations(simulations)
    output.writeIntros()
    create_players(redSox, dodgers)
    inningsR = Inning(redSox, 'R', output, simulations)
    inningsD = Inning(dodgers, 'D', output, simulations)
    dodgerWins = 0
    redSoxWins = 0
    series = 0
    games = 0

    if simulations == 1:
        while redSoxWins < 4 and dodgerWins < 4:
            output.writeGames(games+1)
            while not inningsR.number > 8 or not inningsD.number > 8 or inningsR.runs == inningsD.runs:
                output.inningName('Red Sox', inningsR.number)
                inningsR.playOne()
                output.inningName('Dodgers', inningsD.number)
                inningsD.playOne()
                output.writeScore(inningsR.runs, inningsD.runs)
            games += 1
            if inningsD.runs > inningsR.runs:
                dodgerWins += 1
            else:
                redSoxWins += 1
            print("Game " + str(games) + ": Red Sox " + str(inningsR.runs) + " Dodgers " + str(inningsD.runs))
            inningsR.resetGame()
            inningsD.resetGame()
        if redSoxWins > dodgerWins:
            print("\nRed Sox win the series "+str(redSoxWins)+"-"+str(dodgerWins))
        else:
            print("\nDodgers win the series " + str(dodgerWins) + "-" + str(redSoxWins))

    else:
        rSWinsIn = [0, 0, 0, 0, 0, 0, 0]
        dWinsIn = [0, 0, 0, 0, 0, 0, 0]
        while series < simulations:
            games = 0
            redSoxWins, dodgerWins = 0, 0
            while redSoxWins < 4 and dodgerWins < 4:
                while not inningsR.number > 8 or not inningsD.number > 8 or inningsR.runs == inningsD.runs:
                    inningsR.playOne()
                    inningsD.playOne()
                games += 1
                if inningsD.runs > inningsR.runs:
                    dodgerWins += 1
                else:
                    redSoxWins += 1
                inningsR.resetGame()
                inningsD.resetGame()
            series += 1
            if redSoxWins > dodgerWins:
                output.writeSeries(series, 'Red Sox', games)
                rSWinsIn[games-1] += 1
            else:
                dWinsIn[games-1] += 1
                output.writeSeries(series, 'Dodgers', games)
        for i in range(4):
            print("Dodgers win in " + str(i+4) + " - " + str(round(dWinsIn[i+3] / series * 100, 1)) + "%")
        print()
        for i in range(4):
            print("Red Sox win in " + str(i+4) + " - " + str(round(rSWinsIn[i+3] / series * 100, 1)) + "%")



    output.closeFiles()


main()