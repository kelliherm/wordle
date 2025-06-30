import json
import random

import board

class Game:
    def __init__(self) -> None:      
        self.load_words()
        self.setup_game()

    def destroy_game(self) -> None:
        self.board.destroy_board()

    def get_user_guess(self) -> str:
        return input("What is the player's guess?  ").upper()

        # TODO Add error handling to user guess system, check value word, etc.

    @staticmethod
    def return_guess_complete(self, guess, hidden_word=None) -> list:
        pass

    def load_words(self) -> None:
        words_file = open("wordle\\words.json", "r")  # TODO Figure out python filestructure system for loading words/folder usage
        words = json.load(words_file)
        self.nyt_words = words["nyt_legal"]
        self.all_words = words["all_legal"]
        words_file.close()

    def setup_game(self) -> None:
        self.board = board.Board()
        self.guess_number = 1

    def reset_game(self) -> None:
        self.board.reset_board()
        self.guess_number = 1

    def play_game(self) -> None:
        pass

    def display_game(self) -> None:
        pass

if __name__ == "__main__":
    my_game = Game()