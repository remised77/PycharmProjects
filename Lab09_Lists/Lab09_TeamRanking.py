#
# Written by: Luke Shannon
# 01/29/19
# This program creates team rankings.

class Team:

    """ This is the description. """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def addGame(self, line):
        teams = line.split(' vs ')
        team1 = teams[0]
        team2 = teams[1]
        if str(team) in team1:


    def scoreGames(self):



def inputs():
    filename = input("What would you like to name the file (TeamRankingInput.py)? ") or 'TeamRankingInput.py'
    ranking = input("According to what metric (wins, draws, losses)? ") or "wins"
    trend = input("According to what trend (greatest to least)? ") or "greatest to least"
    return filename, ranking, trend


def readFile(filename):
    infile = open(filename, 'r')
    contents = [infile.readline(), infile.read]
    contents[1].split('\n\n')
    league = contents[0]
    teamList = contents[1]
    teamList.split('\n')
    scores = contents[2]
    scores.split('\n')
    return league, teamList, scores



def main():
    filename, ranking, trend = inputs()
    league, teamList, scores = readFile(filename)
    allTeams = []
    for team in teamList:
        allTeams.append(Team(team))
    for score in scores:
        for team in allTeams:
            if str(team) in score:
                team.addGame(score)

