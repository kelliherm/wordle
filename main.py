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
    
    else:
        print("Command not recognized.")