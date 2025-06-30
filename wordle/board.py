import colorama

class Board:
    def __init__(self, number_of_guesses=6) -> None:
        colorama.init()

        self.number_of_guesses = number_of_guesses

        self.board = [[] for i in range(self.number_of_guesses)]
        self.colors = {
            "GREEN" : colorama.Fore.GREEN,
            "G" : colorama.Fore.GREEN,
            "YELLOW" : colorama.Fore.YELLOW,
            "Y" : colorama.Fore.YELLOW,
            "BLACK" : colorama.Fore.BLACK,
            "B" : colorama.Fore.BLACK,
            "RESET" : colorama.Style.RESET_ALL,
        }
    
    def draw_board(self) -> None:
        for row_index in range(self.number_of_guesses):
            print(row_index + 1, end="  ")
            if self.board[row_index] != []:
                for character_dict in self.board[row_index]:
                    print(self.colors[character_dict["COL"]] + character_dict["CHAR"], end="")
            print(self.colors["RESET"])
    
    def destroy_board(self) -> None:
        colorama.deinit()

    def reset_board(self) -> None:
        self.board = [[] for i in range(self.number_of_guesses)]

    def update_board(self, guess_list, guess_num=None) -> None:
        if guess_num != None:
            self.board[guess_num - 1] = guess_list
        else:
            for row_index in range(self.number_of_guesses):
                if self.board[row_index] == []:
                    self.board[row_index] = guess_list
                    break


if __name__ == "__main__":
    my_board = Board()

    my_board.update_board([{"CHAR" : "S",
                            "COL" : "BLACK",},
                            {"CHAR" : "A",
                             "COL" : "BLACK"},
                            {"CHAR" : "L",
                             "COL" : "BLACK"},
                            {"CHAR" : "E",
                             "COL" : "BLACK"},
                            {"CHAR" : "T",
                             "COL" : "GREEN"}])

    my_board.update_board([{"CHAR" : "G",
                            "COL" : "GREEN",},
                            {"CHAR" : "I",
                             "COL" : "YELLOW"},
                            {"CHAR" : "A",
                             "COL" : "BLACK"},
                            {"CHAR" : "N",
                             "COL" : "BLACK"},
                            {"CHAR" : "T",
                             "COL" : "GREEN"}])
    
    my_board.draw_board()
