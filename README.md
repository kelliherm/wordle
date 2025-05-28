# Wordle Algorithms

A collection of algorithms to solve the game of Wordle. There is currently an algorithm to solve Wordle using the computer, which runs completely by itself. The game itself uses all possible 5 letter words in the English language. Additionally, there is a human playable version of the game. It similarly uses all of possible 5 letter words as a potential hidden word.

The game can be easily played from the command line. In order to do so, enter the following command while in the same directory as `main.py`.

```bash
python main.py human
```

In order to watch the computer attempt to solve the game, enter the following command.

```bash
python main.py computer
```

Example code for both the human playable and the computer playable code can be found is the large code blocks below.

```python
import wordle

myGame = wordle.game.Game()
myGame.Play()
```

In order to have the computer solve the game, the following code is used. It will follow the computer as it tries to win the game.

```python
import wordle

myGame = wordle.solve.ComputerSolve()
myGame.play()
```