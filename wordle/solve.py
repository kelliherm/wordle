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

        words_list = self.game.all_words
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

    def get_top_guesses(self, mode="rw"):
        if "w" in mode:
            result = {}
            for word in self.game.all_words:
                expected_value = self.get_expected_value(word)
                result[word] = expected_value
                print(word, expected_value)
            with open("first_guess.json", "w") as file:
                json.dump(result, file, indent=4)
                file.close()
        
        if "r" in mode:
            try:
                with open("first_guess.json", "r") as file:
                    self.guess_data = json.load(file)
                self.guess_data = sorted(self.guess_data.items(), key=lambda item: item[1], reverse=True)
                print(self.guess_data[0:10])
            except:
                print("File does not exist.")


    def play(self):
        pass

    def reset(self):
        pass

    def setup(self):
        pass


if __name__ == "__main__":
    my_solve = ComputerSolve()

    my_solve.get_top_guesses(mode= "r")
