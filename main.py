from wordlegame import WordleBoard

game = WordleBoard()

gamewon = False
guessnum = 1

game.Intro()
game.DrawBoard()

while (guessnum <= 6) and (gamewon == False):
    guess = game.GetInput()
    game.UpdateBoard(guess, guessnum)
    game.DrawBoard()

    if guess == game.hiddenword:
        print('You won the game!')
        exit()

    guessnum += 1