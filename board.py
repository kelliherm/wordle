import random

class WordleBoard():
    def __init__(self):
        self.green = '\U0001F7E9'
        self.yellow = '\U0001F7E8'
        self.black = '\U00002B1B'
        self.white = '\U00002B1C'

        self.breaksym = '  '

        self.boardchar = {
            '10' : '_', '11' : '_', '12' : '_', '13' : '_', '14' : '_',
            '20' : '_', '21' : '_', '22' : '_', '23' : '_', '24' : '_',
            '30' : '_', '31' : '_', '32' : '_', '33' : '_', '34' : '_',
            '40' : '_', '41' : '_', '42' : '_', '43' : '_', '44' : '_',
            '50' : '_', '51' : '_', '52' : '_', '53' : '_', '54' : '_',
            '60' : '_', '61' : '_', '62' : '_', '63' : '_', '64' : '_',
        }

        self.boardstatus = {
            '10' : self.white, '11' : self.white, '12' : self.white, '13' : self.white, '14' : self.white,
            '20' : self.white, '21' : self.white, '22' : self.white, '23' : self.white, '24' : self.white,
            '30' : self.white, '31' : self.white, '32' : self.white, '33' : self.white, '34' : self.white,
            '40' : self.white, '41' : self.white, '42' : self.white, '43' : self.white, '44' : self.white,
            '50' : self.white, '51' : self.white, '52' : self.white, '53' : self.white, '54' : self.white,
            '60' : self.white, '61' : self.white, '62' : self.white, '63' : self.white, '64' : self.white,
        }

        self.legalwords = []
        legalwordsfile = open('legalwords.txt')
        for line in legalwordsfile:
            self.legalwords.append(line[:-1])
        legalwordsfile.close()

        self.hiddenword = random.choice(self.legalwords)
    
    def DrawBoard(self):
        # Draws the game board with both all of the guesses and all of the markers for placement
        
        print(self.boardchar['10'] + self.boardchar['11'] + self.boardchar['12'] + self.boardchar['13'] + self.boardchar['14'], end='')
        print(self.breaksym, end='')
        print(self.boardstatus['10'] + self.boardstatus['11'] + self.boardstatus['12'] + self.boardstatus['13'] + self.boardstatus['14'])

        print(self.boardchar['20'] + self.boardchar['21'] + self.boardchar['22'] + self.boardchar['23'] + self.boardchar['24'], end='')
        print(self.breaksym, end='')
        print(self.boardstatus['20'] + self.boardstatus['21'] + self.boardstatus['22'] + self.boardstatus['23'] + self.boardstatus['24'])

        print(self.boardchar['30'] + self.boardchar['31'] + self.boardchar['32'] + self.boardchar['33'] + self.boardchar['34'], end='')
        print(self.breaksym, end='')
        print(self.boardstatus['30'] + self.boardstatus['31'] + self.boardstatus['32'] + self.boardstatus['33'] + self.boardstatus['34'])

        print(self.boardchar['40'] + self.boardchar['41'] + self.boardchar['42'] + self.boardchar['43'] + self.boardchar['44'], end='')
        print(self.breaksym, end='')
        print(self.boardstatus['40'] + self.boardstatus['41'] + self.boardstatus['42'] + self.boardstatus['43'] + self.boardstatus['44'])

        print(self.boardchar['50'] + self.boardchar['51'] + self.boardchar['52'] + self.boardchar['53'] + self.boardchar['54'], end='')
        print(self.breaksym, end='')
        print(self.boardstatus['50'] + self.boardstatus['51'] + self.boardstatus['52'] + self.boardstatus['53'] + self.boardstatus['54'])

        print(self.boardchar['60'] + self.boardchar['61'] + self.boardchar['62'] + self.boardchar['63'] + self.boardchar['64'], end='')
        print(self.breaksym, end='')
        print(self.boardstatus['60'] + self.boardstatus['61'] + self.boardstatus['62'] + self.boardstatus['63'] + self.boardstatus['64'])

        print()
    
    def Intro(self):
        pass # All of the intro code is going to go here, explain the game, etc

    def GetInput(self, computer=False, computerinput=None):
        # Functions for both if the computer is guessing and if a human is guessing
        
        if computer == True:
            guess = computerinput.upper()
            return guess

        elif computer == False:
            guess = input('Enter Guess: ').upper()

            if len(guess) != 5:
                print('Guess must be 5 letters')
                guess = self.GetInput()
            
            elif guess not in self.legalwords:
                print('Guess must be in legal words')
                guess = self.GetInput()
        
            return guess
    
    def UpdateBoard(self, guess, guessnum):
        usedletters = []
        
        for index in range(len(guess)):
            location = str(guessnum) + str(index)
            self.boardchar[location] = guess[index]

            if (guess[index] == self.hiddenword[index]):
                self.boardstatus[location] = self.green
            elif (guess[index] in self.hiddenword) and (guess[index] not in usedletters):
                self.boardstatus[location] = self.yellow
            else:
                self.boardstatus[location] = self.black
            
            usedletters.append(guess[index])