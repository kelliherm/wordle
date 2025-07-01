import json
import random

import board

class Game:
    def __init__(self, diffuculty="hard", guess_length=5) -> None:      
        self.difficulty = diffuculty
        self.game_over = False
        self.guess_length = guess_length
        
        self.load_words()
        self.setup_game()

    def destroy_game(self) -> None:
        self.board.destroy_board()

    def get_user_guess(self) -> str:
        return input("What is the player's guess?  ").upper()

        # TODO Add error handling to user guess system, check value word, etc.

    def return_guess_list(self, guess, hidden_word=None) -> list:
        if hidden_word == None:
            hidden_word = self.hidden_word
        
        guess_list = [{"CHAR" : char,
                       "COL" : None} for char in guess]
        
        for index in range(self.guess_length):
            if guess[index] == hidden_word[index]:
                guess_list[index]["COL"] = "GREEN"
            elif guess[index] not in hidden_word:
                guess_list[index]["COL"] = "BLACK"

        return guess_list
    
    def set_hidden_word(self, hidden_word=None):
        if hidden_word != None:
            self.hidden_word = hidden_word
        elif self.difficulty == "hard":
            self.hidden_word = random.choice(self.all_words)
        elif self.difficulty == "easy":
            self.hidden_word = random.choice(self.nyt_words)
        
        # TODO Add edge case testing and error correction

    def load_words(self) -> None:
        words_file = open("wordle\\words.json", "r")  # TODO Figure out python filestructure system for loading words/folder usage
        words = json.load(words_file)
        self.nyt_words = words["nyt_legal"]
        self.all_words = words["all_legal"]
        words_file.close()

    def setup_game(self) -> None:
        self.board = board.Board()
        self.guess_number = 1
        self.set_hidden_word()

    def reset_game(self) -> None:
        self.board.reset_board()
        self.guess_number = 1

    def play_game(self) -> None:
        pass

    def display_game(self) -> None:
        pass

if __name__ == "__main__":
    my_game = Game()

    print(my_game.return_guess_list(guess="SALET"))