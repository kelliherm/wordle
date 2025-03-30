import random
import board

class Game():
    def __init__(self, computer=False, hardmode=True):
        self.gameOver = False
        self.numGuesses = 0
        self.board = board.Board()
        self.difficultyHard = hardmode
        
        self.DefineLegalWords()
        self.hiddenWord = self.DefineHiddenWord(hardmode=self.difficultyHard)
    
    def Play(self) -> None:
        while self.gameOver == False:
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

    def Reset(self, hardmode=True) -> None:
        self.gameOver = False
        self.numGuesses = 0
        self.board.ResetBoard()
        self.hiddenWord = self.DefineHiddenWord(hard=hardmode)

    def DefineLegalWords(self) -> None:
        self.legalWords = []
        legalwordsfile = open("legalwords.txt")
        for line in legalwordsfile:
            if line[-1] == "\n":
                self.legalWords.append(line[:-1])
            else:
                self.legalWords.append(line)
        legalwordsfile.close()
    
    def ReturnLegalWords(self) -> list:
        if self.difficultyHard == True and self.legalWords != None:
            return self.legalWords
        if self.legalWords == None:
            self.DefineLegalWords()
            self.ReturnLegalWords()

    def DefineHiddenWord(self, hardmode=True) -> str:
        if hardmode == True:
            return random.choice(self.legalWords)
        else:
            return random.choice(self.legalWords)

    def GetGuess(self) -> str:
        return input("Enter guess: ").upper()

        # TODO Error correction required

    def DetermineKey(self, guess, answer=None) -> str:
        usedletters = []
        key = ["","","","",""]

        if answer != None:
            secret = answer
        else:
            secret = self.hiddenWord

        for digit in range(5):
            if guess[digit] == secret[digit]:
                key[digit] = "2"
                usedletters.append(guess[digit])

        for digit in range(5):
            if guess[digit] in secret and secret.count(guess[digit]) > usedletters.count(guess[digit]):
                if key[digit] == "":
                    key[digit] = "1"
                    usedletters.append(guess[digit])
            else:
                if key[digit] == "":
                    key[digit] = "0"

        return "".join(key)


if __name__ == "__main__":
    myGame = Game()
    myGame.Play()