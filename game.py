import random
from board import Board

class Game():
    def __init__(self):
        self.gameWon = False
        self.numGuesses = 0
        self.board = Board()
        
        self.DefineLegalWords()
        self.hiddenWord = self.DefineSecretWord()
    
    def Play(self):
        while self.numGuesses < 6 and self.gameWon == False:
            guess = input("Enter Guess: ").upper()
            self.board.UpdateBoard(guess, self.numGuesses + 1)
    
    def DefineLegalWords(self) -> None:
        self.legalWords = []
        legalwordsfile = open('legalwords.txt')
        for line in legalwordsfile:
            self.legalWords.append(line[:-1])
        legalwordsfile.close()
    
    def DefineSecretWord(self) -> str:
        return random.choice(self.legalwords)
