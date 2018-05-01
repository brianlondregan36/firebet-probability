mport random
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
        gameResults = []
        fireBetProgress = []    
        while(outcome != "seven out"):

            roll = self.RollDie()

            if roll == 7 or roll == 11:
                outcome = str(roll) + " win"
                gameResults.append(outcome)
            elif roll == 2 or roll == 3 or roll == 12:
                outcome = str(roll) + " craps"
                gameResults.append(outcome)
            else:
                mark = roll
                while("seven out" not in outcome and "hit point" not in outcome):
                    roll = self.RollDie()
                    if roll == mark:
                        outcome = "hit point " + str(mark)
                        gameResults.append(outcome)

                        if mark not in fireBetProgress:
                            fireBetProgress.append(mark)
                            if len(fireBetProgress) >= self.goal:
                                gameResults.append("HIT FIRE BET")
                                self.fireBetWinner = True

                    elif roll == 7:
                        outcome = "seven out"
                        gameResults.append(outcome)

        self.games.append(gameResults)



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

def RunTest(numSimulations=10, numBins=15):

    simulationResults = []
    for n in range(numSimulations):
        Bob = Gambler(6)
        while Bob.fireBetWinner == False:
            Bob.ShootCraps()

        numGames = len(Bob.games)
        simulationResults.append(numGames)

    print("The median for this data set is", np.median(simulationResults))
    plt.xlabel("Games Played before hitting the Fire Bet")
    plt.ylabel("Number of Simulations")
    plt.hist(simulationResults, numBins)
    plt.show()



RunTest(10000,50)
