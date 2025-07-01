import collections
import json
import random

import board

class Game:
    def __init__(self, diffuculty: str="hard", guess_length: int=5) -> None:      
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

    def return_guess_list(self, guess: str, hidden_word: str=None) -> list:
        if hidden_word == None:
            hidden = self.hidden_word
        else:
            hidden = hidden_word
        
        guess = list(guess)
        hidden = list(hidden)
        
        result = [{"CHAR" : char,
                    "COL" : "BLACK"} for char in guess]
        
        for i in range(self.guess_length):
            if guess[i] == hidden[i]:
                result[i]["COL"] = "GREEN"
                guess[i] = None
                hidden[i] = None
        
        unmatched_counts = collections.Counter(filter(None, hidden))

        for i in range(self.guess_length):
            if guess[i] is not None and unmatched_counts[guess[i]] > 0:
                result[i]["COL"] = "YELLOW"
                unmatched_counts[guess[i]] -= 1

        return result
    
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

    my_game.board.update_board(my_game.return_guess_list("SPEED", hidden_word="ABIDE"))
    my_game.board.update_board(my_game.return_guess_list("SPEED", hidden_word="ERASE"))
    my_game.board.update_board(my_game.return_guess_list("SPEED", hidden_word="STEAL"))
    my_game.board.update_board(my_game.return_guess_list("SPEED", hidden_word="CREPE"))

    my_game.board.draw_board()
