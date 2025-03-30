import math
import game

class ComputerSolve():
    def __init__(self, hardmode=True):
        self.game = game.Game(computer=True, hardmode=hardmode)
        self.legalWords = self.game.ReturnLegalWords()
        self.availibleWords = self.legalWords
        self.rewards = {0 : 0, 1 : 1, 2 : 2, 3 : 3}

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
        options = ["2", "1", "0"]
        total = 0
        n = len(self.availibleWords)

        for i in options:
            for j in options:
                for k in options:
                    for l in options:
                        for m in options:
                            userkey = i + j + k + l + m
                            px = self.GetNumPossibleMatches(userguess, userkey) / n
                            #print(userkey + "   " + str(px))
                            try:
                                total += -1 * px * math.log(px, 2)
                            except:
                                continue
        
        return total

    def GetNumPossibleMatches(self, guess, key) -> int:
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
        
        return len(possible)
        
    def GetListPossibleMatches(self, guess, key) -> list:
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
        
        return possible
    
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

##################
   
    ''''for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position
 
# Sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print(arr)'''

###############
    
    def ReplaceAvailibleWords(self, words) -> None:
        self.availibleWords = words


if __name__ == "__main__":
    myTest = ComputerSolve()
    myTest.game.hiddenWord = "BLARE"

    myGuessA = "CRANE"
    myGuessB = "DOORS"
    
    #myKeyA = myTest.game.DetermineKey(myGuessA)
    #myKeyA = "01202"

    #myKeyB = myTest.game.DetermineKey(meGuessB)
    #myKeyB = "00020"

    #myTest.GetPossibleMatches(myGuessA, myKey)
    
    #myValueA = myTest.GetExpectedValue(myGuessA)
    #myValueB = myTest.GetExpectedValue(myGuessB)

    #print(myValueA)
    #print(myValueB)

    #print(myTest.GetNumPossibleMatches(myGuessA, myTest.game.DetermineKey(myGuessA)))
    #print(myTest.GetNumPossibleMatches(myGuessB, myTest.game.DetermineKey(myGuessB)))

    myTest.GetOptimalGuess()