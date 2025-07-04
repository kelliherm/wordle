import colorama

class Board:
    def __init__(self, number_of_guesses=6) -> None:
        colorama.init()

        self.number_of_guesses = number_of_guesses

        self.board = [[] for i in range(self.number_of_guesses)]
        self.colors = {
            "GREEN" : colorama.Fore.GREEN,
            "YELLOW" : colorama.Fore.YELLOW,
            "BLACK" : colorama.Fore.BLACK,
            "RESET" : colorama.Style.RESET_ALL,
        }
    
    def destroy(self) -> None:
        colorama.deinit()

    def draw(self) -> None:
        for row_index in range(self.number_of_guesses):
            print(row_index + 1, end="  ")
            if self.board[row_index] != []:
                for character_dict in self.board[row_index]:
                    print(self.colors[character_dict["COL"]] + character_dict["CHAR"], end="")
            print(self.colors["RESET"])
    
    def reset(self) -> None:
        self.board = [[] for i in range(self.number_of_guesses)]

    def update(self, guess_list, guess_num=None) -> None:
        if guess_num != None:
            self.board[guess_num - 1] = guess_list
        else:
            for row_index in range(self.number_of_guesses):
                if self.board[row_index] == []:
                    self.board[row_index] = guess_list
                    break


if __name__ == "__main__":
    my_board = Board()

    my_board.update([{"CHAR" : "S",
                            "COL" : "BLACK",},
                            {"CHAR" : "A",
                             "COL" : "BLACK"},
                            {"CHAR" : "L",
                             "COL" : "BLACK"},
                            {"CHAR" : "E",
                             "COL" : "BLACK"},
                            {"CHAR" : "T",
                             "COL" : "GREEN"}])

    my_board.update([{"CHAR" : "G",
                            "COL" : "GREEN",},
                            {"CHAR" : "I",
                             "COL" : "YELLOW"},
                            {"CHAR" : "A",
                             "COL" : "BLACK"},
                            {"CHAR" : "N",
                             "COL" : "BLACK"},
                            {"CHAR" : "T",
                             "COL" : "GREEN"}])
    
    my_board.draw()
