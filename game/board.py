class Board():
    def __init__(self):
        self.colors = ["⬛", "🟨", "🟩"]
        self.board = [[] for i in range(6)]

    def DrawBoard(self):
        print()
        for row in self.board:
            if row != []:
                print(self.board.index(row) + 1, end="")
                print("  ", end="")
                for char in row:
                    print(char[0], end="")
                print("  ", end="")
                for char in row:
                    print(char[1], end="")
                print()
        print()
 
    def UpdateBoard(self, guess_number, guess, key):
        updated_word = []
        for index in range(len(guess)):
            char_key = (guess[index], key[index])
            updated_word.append(char_key)
        self.board[guess_number] = updated_word

    def ResetBoard(self):
        self.board = [[] for i in range(6)]


if __name__ == "__main__":
    myBoard = Board()

    myBoard.UpdateBoard(0, "SALET", "⬛⬛⬛⬛🟩")
    myBoard.UpdateBoard(1, "GIANT", "🟩🟨⬛⬛🟩")

    myBoard.DrawBoard()