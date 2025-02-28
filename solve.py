import game

class Computer():
    def __init__(self, hardmode=True):
        self.game = game.Game(computer=True, hardmode=hardmode)
        self.legalWords = self.game.ReturnLegalWords()
        self.availibleWords = self.legalWords
        self.rewards = {0 : 0, 1 : 1, 2 : 2, 3 : 3}

    def OptimalGuess(self, progress=False):
        values = {}
        n = 0
        for guess in self.availibleWords:
            value = self.ExpectedValue(guess)
            if value in values.keys():
                values[value].append(guess)
            else:
                values[value] = [guess]
            n += 1
            
            if progress == True:
                if n % 100 == 0:
                    print(n)
        
        values = dict(sorted(values.items(), reverse=True))
        #print({k: v for i, (k, v) in enumerate(values.items()) if i < 100})
        return values[next(iter(values))][0]

        # TODO Recognize the fact that multiple words may be returned

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
            score += self.rewards[int(char)]
        
        return score

        # TODO 0 should represent not finding new information, while black may still reward as information. Current system does not take this into account yet

    def TuneScores(self, record=True):
        pass

        # TODO Methodically test different scenerios to find optimal weights

    def OpenScores(self):
        pass

        # TODO Open previously found scores that are located in local text file

    def RemoveIncorrect(self):
        pass

        # TODO Function to remove all the possible words that are no longer eleible given the guesses made


if __name__ == "__main__":
    myTest = Computer()
    #print(myTest.ExpectedValue("CRANE"))
    #print(myTest.ExpectedValue("MAGMA"))
    print(myTest.OptimalGuess(progress=True))