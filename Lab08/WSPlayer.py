#
# Written by Luke Shannon
# 01/20/19
# asd

from random import *

class Player:

    '''d'''

    def __init__(self, fileline, lineup):
        stats = fileline.split('\t')
        self.spot = lineup
        self.lname = stats[0]
        self.fname = stats[1]
        self.name = self.fname[0] + '. ' + self.lname
        self.avg = eval(stats[2])
        self.hits = eval(stats[3])
        self.doubles = eval(stats[4])
        self.triples = eval(stats[5])
        self.homers = eval(stats[6])
        self.nonsingles = self.doubles + self.triples + self.homers
        self.bighits = self.triples + self.homers
        self.atbats = self.hits / self.avg
        self.homerCount = 0

    def __str__(self):
        return self.name

    def swing(self):
        chance = random()
        if self.homers / self.atbats > chance:
            self.homerCount += 1
            return 4
        elif self.bighits / self.atbats > chance:
            return 3
        elif self.nonsingles / self.atbats > chance:
            return 2
        elif self.avg > chance:
            return 1
        else:
            return 0



