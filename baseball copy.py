import re
import sys, os

if len(sys.argv) < 2:
    sys.exit("Usage: {sys.argv[0]} filename")

filename = sys.argv[1]

if not os.path.exists(filename):
    sys.exit("Error: File '{sys.argv[1]}' not found")
class player: 
    def __init__(self, name, bats, hits, runs):
        self.name = name
        self.bats=bats
        self.hits=hits
        self.runs=runs
        self.battingAverage=0.0

    def player_name(self):
        return self.name

    def numBats(self):
        return self.bats

    def numHits(self):
        return self.hits

    def numRuns(self):
        return self.runs

    def addBats(self, bats):
        self.bats= self.bats+bats

    def addHits(self, hits):
        self.hits = self.hits + hits

    def addRuns(self, runs):
        self.runs = self.runs+ runs

    def updateBattingAverage(self):
        average= self.hits/self.bats
        self.battingAverage=average

    def getAverage(self):
        return self.battingAverage

        
stats=set([])
players=set([])

regex_name = re.compile(r"(\w+\s\w+)\sbatted\s(\d) times with (\d) hits and (\d) runs")

def regex_check(test):
    matched = re.search(regex_name, test)
    if matched: 
        x=player(matched.group(1), float(matched.group(2)), float(matched.group(3)), float(matched.group(4)))
        alreadyThere=matched.group(1) in players
        if alreadyThere:
            for stat in stats:
                if matched.group(1) == stat.player_name():
                    stat.addBats(float(matched.group(2)))
                    stat.addHits(float(matched.group(3))) 
                    stat.addRuns(float(matched.group(4)))
                    stat.updateBattingAverage()
        else:
            stats.add(x)
            players.add(x.player_name())

with open(filename, "r") as f: 
        line = f.readline()
        while line: 
            regex_check(line)
            line = f.readline()

sortedStats= sorted(stats, key=lambda stats:stats.battingAverage, reverse=True)
for stat in sortedStats:
    print("{}: {:.3f}".format(stat.player_name(), round(stat.getAverage(), 3)))
