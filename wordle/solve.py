import json
import math

import game

class ComputerSolve:
    def __init__(self, difficulty: str="hard", verbose: bool=False, guess_length: int=5):
        self.game = game.Game(diffuculty=difficulty, guess_length=guess_length, name="Computer")
        self.verbose = verbose
    
    def get_expected_value(self, guess) -> float:
        key_combinations = [i + j + k + l + m
                            for i in ["🟩", "🟨", "⬛"]
                            for j in ["🟩", "🟨", "⬛"]
                            for k in ["🟩", "🟨", "⬛"]
                            for l in ["🟩", "🟨", "⬛"]
                            for m in ["🟩", "🟨", "⬛"]]

        keys = {}
        for key_combination in key_combinations:
            keys[key_combination] = 0

        words_list = self.legalWords
        #words_list = self.availibleWords
        n = len(words_list)

        # TODO Find a better method for determining the words list

        for word in words_list:
            keys[self.game.return_guess_key(guess, hidden_word=word)] += 1

        expected_value = 0

        for key_combination in key_combinations:
            px = keys[key_combination] / n
            if px != 0:
                expected_value += -1 * px * math.log2(px)
        
        return expected_value

    def get_top_guesses(self):
        pass

    def play(self):
        pass

    def reset(self):
        pass

    def setup(self):
        pass


if __name__ == "__main__":
    my_solve = ComputerSolve()
