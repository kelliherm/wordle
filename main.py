import wordle

if __name__ == "__main__":
    import sys
    command = sys.argv[1]

    if command == "human":
        myGame = wordle.game.Game()
        myGame.Play()
    
    elif command == "computer":
        myGame = wordle.solve.ComputerSolve()
        myGame.Play()

    elif command == "computer_all":
        myGame = wordle.solve.ComputerSolve()

        words = []
        wordsfile = open("wordle\\legalwords.txt")
        for line in wordsfile:
            if line[-1] == "\n":
                words.append(line[:-1])
            else:
                words.append(line)
        wordsfile.close()

        for word in words:
            myGame.game.secretWord = word
            data = myGame.Play(return_data=True)
            with open("data.txt", "a") as file:
                file.write(data)
            myGame.ResetGame()
    
    else:
        print("Command not recognized.")