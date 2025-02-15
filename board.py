import colorama

colorama.init()

class Board():
    def __init__(self):
        self.boardColors = [colorama.Fore.BLACK, colorama.Fore.YELLOW, colorama.Fore.GREEN]
        self.board = [[] for i in range(6)]

    def DrawBoard(self):
        print()
        for row in self.board:
            if row != []:
                for char in row:
                    print(self.boardColors[char[0]] + char[1], end="")
                print()
        print()
 
    def UpdateBoard(self, guessnum, userguess, guesskey):
        guess = [(int(guesskey[0]),userguess[0]),(int(guesskey[1]),userguess[1]),(int(guesskey[2]),userguess[2]),(int(guesskey[3]),userguess[3]),(int(guesskey[4]),userguess[4])]
        self.board[guessnum] = guess
