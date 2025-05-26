import random
import board

class Game():
    def __init__(self):
        self.gameOver = False
        self.numGuesses = 0
        self.board = board.Board()
        
        self.DefineLegalWords()
        self.secretWord = self.SetSecretWord()
    
    def Play(self) -> None:
        while self.gameOver == False:
            self.board.DrawBoard()

            print(f"You have {6 - self.numGuesses} remaining.")

            guess = self.GetUserGuess() 
            key = self.DetermineKey(guess)

            self.board.UpdateBoard(self.numGuesses, guess, key)

            self.numGuesses += 1

            if guess == self.secretWord:
                self.board.DrawBoard()
                print(f"You have won the game in {self.numGuesses} guesses!")
                self.gameOver = True
            elif self.numGuesses == 6:
                self.board.DrawBoard()
                print("You have lost the game.")
                print(f"The hidden word was {self.secretWord}.")
                self.gameOver = True

    def ResetGame(self, hardmode=True) -> None:
        self.gameOver = False
        self.numGuesses = 0
        self.board.ResetBoard()
        self.secretWord = self.DefineHiddenWord()

    def DefineLegalWords(self) -> None:
        self.legalWords = []
        legalwordsfile = open("legalwords.txt")
        for line in legalwordsfile:
            if line[-1] == "\n":
                self.legalWords.append(line[:-1])
            else:
                self.legalWords.append(line)
        legalwordsfile.close()

    def SetSecretWord(self) -> str:
        return random.choice(self.legalWords)

    def GetUserGuess(self) -> str:
        return input("Enter guess: ").upper()

        # TODO Error correction required

    def DetermineKey(self, guess, answer=None) -> str:
        usedletters = []
        key = ["","","","",""]

        # Allows for standalone functionality
        if answer != None:
            secret = answer
        else:
            secret = self.secretWord

        for digit in range(5):
            if guess[digit] == secret[digit]:
                key[digit] = "🟩"
                usedletters.append(guess[digit])

        for digit in range(5):
            if guess[digit] in secret and secret.count(guess[digit]) > usedletters.count(guess[digit]):
                if key[digit] == "":
                    key[digit] = "🟨"
                    usedletters.append(guess[digit])
            else:
                if key[digit] == "":
                    key[digit] = "⬛"

        return "".join(key)


if __name__ == "__main__":
    myGame = Game()
    myGame.Play()