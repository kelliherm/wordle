import game

class Computer():
    def __init__(self, hardmode=True):
        self.game = game.Game(computer=True, hardmode=hardmode)
        self.legalWords = self.game.ReturnLegalWords()
        self.availibleWords = self.legalWords

    def ExpectedValue(self, guess) -> int:
        scatterplot = {}
        for word in self.legalWords:
            key = self.game.DetermineKey(guess, answer=word)
            score = self.GetScore(key)
            if score in scatterplot.keys():
                scatterplot[score] += 1
            else:
                scatterplot[score] = 1

        expectedvalue = 0
        for score, count in scatterplot.items():
            expectedvalue += score * count
        
        return expectedvalue
    
    def GetScore(self, key) -> int:
        score = 0
        for char in key:
            score += int(char)
        
        return score

    def Sort(self) -> None:
        pass


if __name__ == "__main__":
    myTest = Computer()
    print(myTest.ExpectedValue("CRANE"))
    print(myTest.ExpectedValue("MAGMA"))