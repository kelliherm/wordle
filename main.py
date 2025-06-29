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
        all_words = myGame.legalWords
        for word in all_words:
            myGame.game.secretWord = word
            data = myGame.Play(return_data=True)
            with open("data.txt", "a") as file:
                file.write(data)
    
    else:
        print("Command not recognized.")