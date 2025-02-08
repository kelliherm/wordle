from wordlegame import Wordle

game = Wordle()

hiddenword = 'CRANE'
game.hiddenword = hiddenword

gamewon = False
guessnum = 1

game.Intro()
game.DrawBoard()

while (guessnum <= 6) and (gamewon == False):
    guess = game.GetInput()
    game.UpdateBoard(guess, guessnum)
    game.DrawBoard()

    if guess == hiddenword:
        print('You won the game!')
        exit()

    guessnum += 1