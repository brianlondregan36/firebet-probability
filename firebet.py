import random
import numpy as np
import matplotlib.pyplot as plt

class Gambler(object):

    def __init__(self, goal):
        self.goal = goal
        self.fireBetWinner = False
        self.games = []

    def RollDie(self):
        die1 = random.choice([1,2,3,4,5,6])
        die2 = random.choice([1,2,3,4,5,6])
        return die1 + die2
        
    def ShootCraps(self):

        outcome = ""
        results = []
        fireBetProgress = []
        
        while(outcome != "seven out"):

            roll = self.RollDie()

            if roll == 7 or roll == 11:
                outcome = str(roll) + " win"
                results.append(outcome)
            elif roll == 2 or roll == 3 or roll == 12:
                outcome = str(roll) + " craps"
                results.append(outcome)
            else:
                mark = roll
                while("seven out" not in outcome and "hit point" not in outcome):
                    roll = self.RollDie()
                    if roll == mark:
                        outcome = "hit point " + str(mark)
                        results.append(outcome)

                        if mark not in fireBetProgress:
                            fireBetProgress.append(mark)
                            if len(fireBetProgress) >= self.goal:
                                results.append("HIT FIRE BET")
                                self.fireBetWinner = True

                    elif roll == 7:
                        outcome = "seven out"
                        results.append(outcome)

        self.games.append(results)



def UnitTest():
    
    Steve = Gambler(6)
    
    while Steve.fireBetWinner == False:
        Steve.ShootCraps()

    flags = 0
    for game in Steve.games:
        print(game)
        for result in game:
            if result == "HIT FIRE BET":
                flags += 1

    print(flags)

def RunExperiment(numSimulations=10, numBins=15):

    simulationResults = []
    for n in range(numSimulations):
        Bob = Gambler(6)
        while Bob.fireBetWinner == False:
            Bob.ShootCraps()

        gamesPlayedToWin = len(Bob.games)
        simulationResults.append(gamesPlayedToWin)

    medianGames = np.median(simulationResults)
    plt.xlabel("Games Played before hitting the Fire Bet")
    plt.ylabel("Number of Simulations")
    plt.hist(simulationResults, numBins)
    plt.show()
    
    sumGames = np.sum(simulationResults)
    empiricalProb = numSimulations / sumGames
    ratio = 1 / empiricalProb

    print("Median:", medianGames)
    print("Empirical Probability:", empiricalProb)
    print("1 in", ratio, "games")

RunExperiment(10000,200)
