import math
import json
import game

class ComputerSolve():
    def __init__(self):
        self.game = game.Game()
        self.legalWords = self.game.legalWords
        self.availibleWords = self.legalWords

    def GetExpectedValue(self, userguess) -> float:
        options = ["🟩", "🟨", "⬛"]
        wordslist = self.legalWords
        n = len(wordslist)
        keys = {}
        for i in options:
            for j in options:
                for k in options:
                    for l in options:
                        for m in options:
                            keys[i + j + k + l + m] = 0

        for word in wordslist:
            keys[self.game.DetermineKey(userguess, word)] += 1

        expected_val = 0

        for i in options:
            for j in options:
                for k in options:
                    for l in options:
                        for m in options:
                            px = keys[i + j + k + l + m] / n
                            if px != 0:
                                expected_val += -1 * px * math.log2(px)
        
        return expected_val

    def GetOptimalGuess(self) -> str:
        possibleguesses = {}
        wordslist = self.legalWords
        for word in wordslist:
            possibleguesses[word] = self.GetExpectedValue(word)

        '''with open("data.json", "w") as file:
            json.dump(possibleguesses, file, indent=4)

        with open("data.json", "r") as file:
            possibleguesses = json.load(file)'''

        sortedwordlist = sorted(possibleguesses.items(), key=lambda item: item[1], reverse=True)

        return sortedwordlist[0][0]


if __name__ == "__main__":
    myTest = ComputerSolve()

    #myTest.game.hiddenWord = "BLARE"

    #myGuessA = "CRANE"
    #myGuessB = "DOORS"
    
    #myKeyA = myTest.game.DetermineKey(myGuessA)
    #myKeyA = "01202"

    #myKeyB = myTest.game.DetermineKey(meGuessB)
    #myKeyB = "00020"

    #myTest.GetPossibleMatches(myGuessA, myKey)
    
    #myValueA = myTest.GetExpectedValue(myGuessA)
    #myValueB = myTest.GetExpectedValue(myGuessB)

    #print(myValueA)
    #print(myValueB)

    import time

    start_time = time.perf_counter()

    #print(myTest.GetNumPossibleMatches(myGuessA, myTest.game.DetermineKey(myGuessA)))
    #print(myTest.GetNumPossibleMatches(myGuessB, myTest.game.DetermineKey(myGuessB)))

    print(myTest.GetOptimalGuess())

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    print(f"Elapsed time: {elapsed_time:.4f} seconds")

    #print(myTest.game.DetermineKey("SPEED", answer="ABIDE"))
    #print(myTest.game.DetermineKey("SPEED", answer="ERASE"))
    #print(myTest.game.DetermineKey("SPEED", answer="STEAL"))
    #print(myTest.game.DetermineKey("SPEED", answer="CREPE"))