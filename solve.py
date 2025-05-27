import math
import json
import game

class ComputerSolve():
    def __init__(self):
        self.game = game.Game()
        self.legalWords = self.game.legalWords
        self.availibleWords = self.legalWords
        self.information = []
        self.gameOver = False
        self.turn = 0
    
    def Play(self):
        while self.gameOver == False:
            print(f"It is turn number {self.turn + 1}.")
            
            self.game.board.DrawBoard()
            
            if self.turn == 0:
                guess = self.GetOptimalGuess(first_guess=True)
            else:
                guess = self.GetOptimalGuess()
            key = self.game.DetermineKey(guess)

            self.game.board.UpdateBoard(self.turn, guess, key)
            self.information.append((guess, key))

            self.RemoveExtraWords(self.information)

            self.turn += 1

            if guess == self.game.secretWord:
                self.game.board.DrawBoard()
                print(f"The computer has won the game in {self.turn} guesses!")
                self.gameOver = True
            elif self.turn == 6:
                self.game.board.DrawBoard()
                print("The computer has lost the game.")
                print(f"The hidden word was {self.game.secretWord}.")
                self.gameOver = True
    
    def ResetGame(self):
        self.game = game.Game()
        self.legalWords = self.game.legalWords
        self.availibleWords = self.legalWords
        self.information = []
        self.gameOver = False
        self.turn = 0

    def GetExpectedValue(self, userguess) -> float:
        options = ["🟩", "🟨", "⬛"]
        #wordslist = self.legalWords
        wordslist = self.availibleWords
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

    def GetOptimalGuess(self, first_guess=False) -> str:
        if first_guess == True:
            with open("data.json", "r") as file:
                possibleguesses = json.load(file)

            sortedwordlist = sorted(possibleguesses.items(), key=lambda item: item[1], reverse=True)

            return sortedwordlist[0][0]

        possibleguesses = {}
        #wordslist = self.legalWords
        wordslist = self.availibleWords
        for word in wordslist:
            possibleguesses[word] = self.GetExpectedValue(word)

        '''with open("data.json", "w") as file:
            json.dump(possibleguesses, file, indent=4)

        with open("data.json", "r") as file:
            possibleguesses = json.load(file)'''

        sortedwordlist = sorted(possibleguesses.items(), key=lambda item: item[1], reverse=True)

        return sortedwordlist[0][0]
    
    def RemoveExtraWords(self, information_list) -> None:
        wordslist = self.availibleWords
        words_to_remove = []
        for word in wordslist:
            if self.IsWordPossible(word, information_list) == False:
                words_to_remove.append(word)
        for word in words_to_remove:
            self.availibleWords.remove(word)
        print(f"The number of possible answers is {len(self.availibleWords)}")

    def IsWordPossible(self, word, information_list) -> bool:
        for information in information_list:
            usedletters = []
            for index in range(len(word)):
                if word[index] == information[0][index] and information[1][index] == "🟩":
                    pass
                elif word[index] != information[0][index] and information[1][index] == "🟩":
                    return False
                # TODO Get functionality surround yellow letters working
                #elif word[index] in information[0] and information[1][index] == "🟨":
                #    usedletters.append(word[index])
                elif word[index] == information[0][index] and information[1][index] == "🟨":
                    return False
                elif word[index] == information[0][index] and information[1][index] == "⬛":
                    return False
        return True


if __name__ == "__main__":
    myTest = ComputerSolve()

    import time

    start_time = time.perf_counter()

    myTest.Play()

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    print(f"Elapsed time: {elapsed_time:.4f} seconds")