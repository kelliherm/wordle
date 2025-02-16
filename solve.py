import game

class Computer():
    def __init__(self, hardmode=True):
        self.game = game.Game(computer=True, hard=hardmode)
        self.legalWords = self.game.ReturnLegalWords()
        self.availibleWords = self.legalWords

    def ExpectedValue(self, guess) -> int:
        for word in self.legalWords:
            score = self.GetScore(word, self.game.DetermineKey(guess, word))
    
    def GetScore(guess, key) -> int:
        pass

    def Sort(self) -> None:
        pass