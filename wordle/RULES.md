# Rules of Wordle

Wordle is a game in which the player has 6 attempts to guess a 5 letter word. Each guess reveals information to the player on the correctness of a particular letter.

A green letter rewards a correct letter located in the correct positions, while a yellow letter rewards a letter that is in the hidden word but placed in an incorrect position. A black letter signifies the absence of a letter in the hidden word.

## Edge cases

There are several edge cases that may come up in the course of a game. Each edge case is handled the same way, ensuring that information is presented the same for every game.

| Guess | Answer | Expected Result |
|--|--|--|
| SPEED | ABIDE | ⬛⬛🟨⬛🟨 |
| SPEED | ERASE | 🟨⬛🟨🟨⬛ |
| SPEED | STEAL | 🟩⬛🟩⬛⬛ |
| SPEED | CREPE | ⬛🟨🟩🟨⬛ |