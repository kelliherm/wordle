import random
import board

class Game():
    def __init__(self):
        self.gameOver = False
        self.numGuesses = 0
        self.board = board.Board()
        
        self.DefineLegalWords()
        self.hiddenWord = self.DefineHiddenWord()
    
    def Play(self):
        while self.numGuesses < 6 and self.gameOver == False:
            self.board.DrawBoard()
            print(f"You have {6 - self.numGuesses} remaining.")
            guess = self.GetGuess() 

            key = self.DetermineKey(guess)

            self.board.UpdateBoard(self.numGuesses, guess, key)

            self.numGuesses += 1

            if guess == self.hiddenWord:
                self.board.DrawBoard()
                print(f"You have won the game in {self.numGuesses} guesses!")
                self.gameOver = True
            elif self.numGuesses == 6:
                self.board.DrawBoard()
                print("You have lost the game.")
                print(f"The hidden word was {self.hiddenWord}.")
                self.gameOver = True

    def DefineLegalWords(self) -> None:
        self.legalWords = []
        legalwordsfile = open("legalwords.txt")
        for line in legalwordsfile:
            self.legalWords.append(line[:-1])
        legalwordsfile.close()
    
    def DefineHiddenWord(self) -> str:
        return random.choice(self.legalWords)

    def GetGuess(self) -> str:
        return input("Enter guess: ").upper()

        # TODO Error correction required

    def DetermineKey(self, guess) -> str:
        usedletters = []
        key = ["","","","",""]

        for digit in range(5):
            if guess[digit] == self.hiddenWord[digit]:
                key[digit] = "2"
                usedletters.append(guess[digit])

        for digit in range(5):
            if guess[digit] in self.hiddenWord and self.hiddenWord.count(guess[digit]) > usedletters.count(guess[digit]):
                if key[digit] == "":
                    key[digit] = "1"
                    usedletters.append(guess[digit])
            else:
                if key[digit] == "":
                    key[digit] = "0"

        return "".join(key)


if __name__ == "__main__":
    myGame = Game()
    myGame.hiddenWord = "SWALY"
    myGame.Play()