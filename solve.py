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
            keys[self.game.DetermineKey(userguess, answer=word)] += 1

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
    
    def RemoveExtraWords(self, information) -> None:
        pass

    def IsWordPossible(self, word, information_list) -> bool:
        for information in information_list:
            for index in range(len(word)):
                if word[index] == information[0][index] and information[1][index] == "🟩":
                    pass
                # Statement to determine yellows
                elif word[index] == information[0][index] and information[1][index] == "⬛":
                    return False
        return True


if __name__ == "__main__":
    myTest = ComputerSolve()

    import time

    start_time = time.perf_counter()

    #myGuessA = "CRANE"
    #myGuessB = "DOORS"
    
    #myValueA = myTest.GetExpectedValue(myGuessA)
    #myValueB = myTest.GetExpectedValue(myGuessB)

    #print(myValueA)
    #print(myValueB)

    #print(myTest.GetOptimalGuess())

    print(myTest.IsWordPossible("DRONE", [("CRANE", "⬛🟩⬛🟩🟩")]))
    print(myTest.IsWordPossible("DRONE", [("MAGMA", "⬛⬛⬛⬛⬛"), ("DOORS", "🟩⬛🟩🟨⬛")]))
    print(myTest.IsWordPossible("LIONS", [("MAGMA", "⬛⬛⬛⬛⬛"), ("DOORS", "🟩⬛🟩🟨⬛")]))

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    print(f"Elapsed time: {elapsed_time:.4f} seconds")