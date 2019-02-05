#
# Written by: Luke Shannon
# 01/29/19
# This program creates team rankings.


class Team:

    """ This is the description. """

    def __init__(self, name, ranking):
        self.name = name
        self.ranking = ranking
        self.wins = 0
        self.losses = 0
        self.draws = 0

    def __str__(self):
        return self.name

    def addGame(self, line):
        teams = line.split(' vs ')
        team1 = teams[0]
        team2 = teams[1]
        if self.name in team1:
            thisTeam = team1
            otherTeam = team2
        elif self.name in team2:
            thisTeam = team2
            otherTeam = team1
        thisScore = thisTeam.split(' ')
        thisScore.reverse()
        otherScore = otherTeam.split(' ')
        otherScore.reverse()
        if eval(thisScore[0]) > eval(otherScore[0]):
            self.wins += 1
        elif eval(thisScore[0]) == eval(otherScore[0]):
            self.draws += 1
        elif eval(thisScore[0]) < eval(otherScore[0]):
            self.losses += 1

    def getScores(self):
        if self.ranking == 'Wins':
            return self.wins
        if self.ranking == 'Draws':
            return self.draws
        if self.ranking == 'Losses':
            return self.losses


def inputs():
    print()
    filename = input("What is the name of the input file (TeamRankingInput.py)? ") or 'TeamRankingInput.py'
    ranking = input("According to what metric ((Wins), Draws, Losses)? ") or "Wins"
    trend = input("According to what trend ((greatest to least), least to greatest)? ") or "greatest to least"
    return filename, ranking, trend


def readFile(filename):
    infile = open(filename, 'r')
    league = infile.readline()
    contents = infile.read()
    contents = contents.split('\n\n')
    teamList = contents[0].split('\n')
    scores = contents[1].split('\n')
    return league, teamList, scores


def printScores(league, ranking, allTeams, trend):
    if trend == "least to greatest": trend = 'Fewest'
    else: trend = 'Most'
    print('\n')
    print(league[:-1] + ' Ranking by {} {}'.format(trend, ranking))
    print()
    print('Team                W   D   L')
    print('----                -   -   -')
    for team in allTeams:
        print('{:<20}{}   {}   {}'.format(str(team), str(team.wins), str(team.draws), str(team.losses)))


def main():
    filename, ranking, trend = inputs()
    league, teamList, scores = readFile(filename)
    allTeams = []
    for team in teamList:
        allTeams.append(Team(team, ranking))
    for score in scores:
        for team in allTeams:
            if str(team) in score:
                team.addGame(score)
    allTeams.sort(key=lambda team: str(team))
    allTeams.sort(key=lambda team: team.getScores())
    if not trend == 'least to greatest': allTeams.reverse()
    printScores(league, ranking, allTeams, trend)


main()

