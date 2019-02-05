#
# Written by: Luke Shannon
# 01/29/19
# This program ranks teams according to wins, losses, draws, and the preferred trend.


class Team:

    """ This class contains all the information for one team, including the name and team scores.
    Use addGame() to add a score """

    def __init__(self, name, ranking):
        # Prepares the name of the team, the way the teams will be ranked (w/d/l) and sets all variables to 0.
        self.name = name
        self.ranking = ranking
        self.wins = 0
        self.losses = 0
        self.draws = 0

    def __str__(self):
        # Returns the name of the team when called with str() in order to access the name of the team more easily.
        return self.name

    def addGame(self, line):
        # This method takes the full line of a game and adds the appropriate outcome to this team's total.
        teams = line.split(' vs ')
        team1 = teams[0]
        team2 = teams[1]
        # Set thisTeam equal to the team that this instance of class is referring to.
        if self.name in team1:
            thisTeam = team1
            otherTeam = team2
        elif self.name in team2:
            thisTeam = team2
            otherTeam = team1
        # Split and reverse the score so that the score is the first item in a list.
        thisScore = thisTeam.split(' ')
        thisScore.reverse()
        otherScore = otherTeam.split(' ')
        otherScore.reverse()
        # Evaluate the scores and add the appropriate outcome.
        if eval(thisScore[0]) > eval(otherScore[0]):
            self.wins += 1
        elif eval(thisScore[0]) == eval(otherScore[0]):
            self.draws += 1
        elif eval(thisScore[0]) < eval(otherScore[0]):
            self.losses += 1

    def getScores(self):
        # This method returns the total outcomes of the games according to the ranking for sorting purposes in main().
        if self.ranking == 'Losses':
            return self.losses
        elif self.ranking == 'Draws':
            return self.draws
        else:
            return self.wins

def inputs():
    # This function gets the inputs from the user (and sets defaults in case the user does not enter anything).
    print()
    filename = input("What is the name of the input file (TeamRankingInput.py)? ") or 'TeamRankingInput.py'
    ranking = input("According to what metric ((Wins), Draws, Losses)? ") or "Wins"
    trend = input("According to what trend ((greatest to least), least to greatest)? ") or "greatest to least"
    return filename, ranking, trend


def readFile(filename):
    # This function reads the file that the user inputs and splits it, returning the league, teamList, and scores.
    infile = open(filename, 'r')
    # League is equal to the first line of the file.
    league = infile.readline()
    contents = infile.read()
    # Split the contents at the relevant breaks in order to find the teamList and scores.
    contents = contents.split('\n\n')
    teamList = contents[0].split('\n')
    scores = contents[1].split('\n')
    infile.close()
    return league, teamList, scores


def printScores(league, ranking, allTeams, trend):
    # This function prints the organized information back out to the user.
    # This if statement establishes a variable to print 'Most' or 'Fewest' according to the trend.
    if trend == "least to greatest": trend = 'Fewest'
    else: trend = 'Most'
    # These print statements print the standard header of the information.
    print('\n')
    print(league[:-1] + ' Ranking by {} {}'.format(trend, ranking))
    print()
    print('Team                W   D   L')
    print('----                -   -   -')
    # This for loop prints each teams wins, losses, and draws, according to the sorting in allTeams.
    for team in allTeams:
        print('{:<20}{}   {}   {}'.format(str(team), str(team.wins), str(team.draws), str(team.losses)))


def main():
    # This is the main function.
    # Get the inputs from the user.
    filename, ranking, trend = inputs()
    # Read the file to access the teams
    league, teamList, scores = readFile(filename)
    # Add each team to a list.
    allTeams = []
    for team in teamList:
        allTeams.append(Team(team, ranking))
    # Add the score of each game to each team that participated in that game.
    for score in scores:
        for team in allTeams:
            if str(team) in score:
                team.addGame(score)
    # As the teams are sorted from least to greatest through the sort()s below,
    # they should always be reversed unless the trend is 'least to greatest'.
    if not trend == 'least to greatest': gtl = True
    else: gtl = False
    # Sort the teams alphabetically, and then according to their scores and the ranking metric.
    allTeams.sort(key=lambda team: str(team))
    allTeams.sort(key=lambda team: team.getScores(), reverse=gtl)
    # Call the printScores() function to print the scores to the user.
    printScores(league, ranking, allTeams, trend)


main()

