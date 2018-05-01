import random
import matplotlib.pyplot as plt

class Gambler(object):

    def __init__(self, wallet):
        self.wallet = wallet
        self.fireBetHits = [0,0,0]
        self.winLossHistory = []

    def RollDie(self):
        die1 = random.choice([1,2,3,4,5,6])
        die2 = random.choice([1,2,3,4,5,6])
        return die1 + die2

    def ChipStackChange(self, bet, result, winnings):
        self.wallet += (bet + winnings)
        winLoss = (result, winnings, self.wallet)
        self.winLossHistory.append(winLoss)

    def ShootCraps(self, passLineBet, fireBet):

        self.wallet -= fireBet
        fireBetProgress = []

        result = "" 
        while(result != "seven out"):

            self.wallet -= passLineBet
            winnings = 0

            roll = self.RollDie()

            if roll == 7 or roll == 11:
                result = str(roll) + " win"
                winnings = 1 * passLineBet
                self.ChipStackChange(passLineBet, result, winnings)
            elif roll == 2 or roll == 3 or roll == 12:
                result = str(roll) + " craps"
                winnings = 0
                self.ChipStackChange(0, result, winnings)
            else:
                mark = roll
                while("seven out" not in result and "hit point" not in result):
                    roll = self.RollDie()
                    if roll == mark:
                        result = "hit point " + str(mark)
                        winnings = 1 * passLineBet
                        self.ChipStackChange(passLineBet, result, winnings)
                        if fireBet and fireBet > 0 and mark not in fireBetProgress:
                            fireBetProgress.append(mark)
                            if len(fireBetProgress) == 4:
                                winnings = 24 * fireBet
                                self.ChipStackChange(fireBet, "fire bet 4 hit payout", winnings)
                                self.fireBetHits[0] += 1
                            elif len(fireBetProgress) == 5:
                                winnings = 249 * fireBet
                                self.ChipStackChange(fireBet, "fire bet 5 hit payout", winnings)
                                self.fireBetHits[1] += 1
                            elif len(fireBetProgress) == 6:
                                winnings = 999 * fireBet
                                self.ChipStackChange(fireBet, "fire bet 6 hit payout", winnings)
                                self.fireBetHits[2] += 1
                    elif roll == 7:
                        result = "seven out"
                        winnings = 0
                        self.ChipStackChange(0, result, winnings)



minimumBet = 10

def UnitTest():
    Steve = Gambler(100)
    print(Steve.wallet, Steve.fireBetHits, Steve.winLossHistory)
    Steve.ShootCraps(minimumBet,5)
    print(Steve.wallet, Steve.fireBetHits, Steve.winLossHistory)

def ChartWallet():
    John = Gambler(500)
    x, y = [], []
    attempts = 0
    while(John.fireBetHits[2] == 0):
        John.ShootCraps(minimumBet, 5)
        attempts += 1
        x.append(attempts)
        y.append(John.wallet)

    print("Took " + str(attempts) + " number of games.")
    print("Player walked away with $" + John.wallet if John.wallet[0] != "-" else "Player walked away with -$" + John.wallet[1:len(John.wallet)])
    plt.plot(x, y)
    plt.xlabel("Craps Games Played")
    plt.ylabel("Player's Wallet")
    plt.show()



ChartWallet()
