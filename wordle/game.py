import collections
import json
import os
import platform
import random

import board

class Game:
    def __init__(self, diffuculty: str="hard", guess_length: int=5, name: str="Player") -> None:      
        self.difficulty = diffuculty
        self.guess_length = guess_length

        self.name = name

        self.load_words()
        self.setup()

    def destroy(self) -> None:
        self.board.destroy()

    def display(self, message="") -> None:
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")
        if message != "":
            print(message)
        self.board.draw()

    def get_user_guess(self) -> str:
        return input(f"What is {self.name}'s guess?  ").upper()

        # TODO Add error handling to user guess system, check value word, etc.

    def load_words(self) -> None:
        words_file = open("wordle\\words.json", "r")  # TODO Figure out python filestructure system for loading words/folder usage
        words = json.load(words_file)
        self.nyt_words = words["nyt_legal"]
        self.all_words = words["all_legal"]
        words_file.close()

    def play(self) -> None:
        while not self.game_over:
            self.display(message=f"It is guess number {self.guess_number}.")
            guess = self.get_user_guess()

            guess_key = self.return_guess_key(guess)

            self.board.update(self.return_guess_list(guess, guess_key))

            if guess == self.hidden_word:
                self.game_over = True
                self.display(message=f"{self.name} has won the game. It took {self.guess_number} to guess the hidden word.")

            self.guess_number += 1
            if self.guess_number > 6:
                self.game_over = True
                self.display(message=f"{self.name} has lost the game. The hidden word was {self.hidden_word}.")
        
        answer = input("Would you like to play again? [Y/n]  ").lower()
        if answer in ("yes", "y"):
            self.reset()
        else:
            self.destroy()

    def reset(self) -> None:
        self.board.reset()
        self.game_over = False
        self.guess_number = 1
        self.set_hidden_word()
        self.play()

    def set_hidden_word(self, hidden_word=None):
        if hidden_word != None:
            self.hidden_word = hidden_word
        elif self.difficulty == "hard":
            self.hidden_word = random.choice(self.all_words)
        elif self.difficulty == "easy":
            self.hidden_word = random.choice(self.nyt_words)
        
        # TODO Add edge case testing and error correction

    def setup(self) -> None:
        self.board = board.Board()
        self.game_over = False
        self.guess_number = 1
        self.set_hidden_word()

    def return_guess_key(self, guess: str, hidden_word: str=None) -> str:
        if hidden_word == None:
            hidden = self.hidden_word
        else:
            hidden = hidden_word
        
        guess = list(guess)
        hidden = list(hidden)
        
        result = ["⬛" for char in guess]
        
        for i in range(self.guess_length):
            if guess[i] == hidden[i]:
                result[i] = "🟩"
                guess[i] = None
                hidden[i] = None
        
        unmatched_counts = collections.Counter(filter(None, hidden))

        for i in range(self.guess_length):
            if guess[i] is not None and unmatched_counts[guess[i]] > 0:
                result[i] = "🟨"
                unmatched_counts[guess[i]] -= 1

        return "".join(result)

    def return_guess_list(self, guess: str, key: str) -> list:
        key_map = {
            "🟩" : "GREEN",
            "🟨" : "YELLOW",
            "⬛" : "BLACK",
        }

        result = [{"CHAR" : guess[index],
                    "COL" : key_map[key[index]]} for index in range(self.guess_length)]
        
        return result
    

if __name__ == "__main__":
    my_game = Game(diffuculty="easy")

    #my_game.board.update_board(my_game.return_guess_list("SPEED", hidden_word="ABIDE"))
    #my_game.board.update_board(my_game.return_guess_list("SPEED", hidden_word="ERASE"))
    #my_game.board.update_board(my_game.return_guess_list("SPEED", hidden_word="STEAL"))
    #my_game.board.update_board(my_game.return_guess_list("SPEED", hidden_word="CREPE"))

    my_game.play()
