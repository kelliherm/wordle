import math
import game

class ComputerSolve():
    def __init__(self):
        self.game = game.Game()
        self.legalWords = self.game.legalWords
        self.availibleWords = self.legalWords

    def GetOptimalGuess(self) -> str:
        allpossibleguesses = []
        total = len(self.availibleWords)
        n = 1
        for possibleguess in self.availibleWords:
            value = self.GetExpectedValue(possibleguess)
            allpossibleguesses.append((value, possibleguess))
            print(str(n) + " / " + str(total))
            n += 1
        
        #return self.InsertionSort(allpossibleguesses)
        print(self.InsertionSort(allpossibleguesses))

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

    def GetNumPossibleMatches(self, guess, key) -> int:
        possible = []

        for word in self.availibleWords:
            flag = 0
            for index in range(5):
                if key[index] == "🟩" and guess[index] == word[index]:
                    flag += 1
                elif key[index] == "🟨" and guess[index] in word:
                    flag += 1
            if flag > 0:
                possible.append(word)
        
        return len(possible)
        
    '''def GetListPossibleMatches(self, guess, key) -> list:
        possible = []

        for word in self.availibleWords:
            flag = 0
            for index in range(5):
                if key[index] == "2" and guess[index] == word[index]:
                    flag += 1
                elif key[index] == "1" and guess[index] in word:
                    flag += 1
            if flag > 0:
                possible.append(word)
        
        return possible'''
    
    def InsertionSort(self, unsorted) -> list:
        n = len(unsorted)

        if n <= 1:
            return unsorted
        
        for i in range(1, n):
            key = unsorted[i][1]
            j = i - 1
            while j >= 0 and key < unsorted[j][1]:
                unsorted[j + 1] = unsorted[j]
                j -= 1
            unsorted[j + 1] = unsorted[j]
        
        return unsorted


if __name__ == "__main__":
    myTest = ComputerSolve()

    #myTest.game.hiddenWord = "BLARE"

    myGuessA = "CRANE"
    myGuessB = "DOORS"
    
    #myKeyA = myTest.game.DetermineKey(myGuessA)
    #myKeyA = "01202"

    #myKeyB = myTest.game.DetermineKey(meGuessB)
    #myKeyB = "00020"

    #myTest.GetPossibleMatches(myGuessA, myKey)
    
    myValueA = myTest.GetExpectedValue(myGuessA)
    myValueB = myTest.GetExpectedValue(myGuessB)

    print(myValueA)
    print(myValueB)

    #print(myTest.GetNumPossibleMatches(myGuessA, myTest.game.DetermineKey(myGuessA)))
    #print(myTest.GetNumPossibleMatches(myGuessB, myTest.game.DetermineKey(myGuessB)))

    #myTest.GetOptimalGuess()

    #print(myTest.game.DetermineKey("SPEED", answer="ABIDE"))
    #print(myTest.game.DetermineKey("SPEED", answer="ERASE"))
    #print(myTest.game.DetermineKey("SPEED", answer="STEAL"))
    #print(myTest.game.DetermineKey("SPEED", answer="CREPE"))