Some LLM generated hangman adapted to use a words file.

Download and run (assumes you have Git and Python):
```
$ git clone https://github.com/judwhite/py-hangman.git
$ cd py-hangman
$ python main.py
```

Example game:
```
C H E S S - H A N G M A N

  +---+
  |   |
      |
      |
      |
      |
=========

Missed letters: 
_ _ _ _ _ _ _ _ _ 

Guess a letter: e

  +---+
  |   |
  O   |
      |
      |
      |
=========

Missed letters: E 
_ _ _ _ _ _ _ _ _ 

Guess a letter: a

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

Missed letters: E A 
_ _ _ _ _ _ _ _ _ 

Guess a letter: i

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

Missed letters: E A 
_ _ _ _ _ _ I _ _ 

Guess a letter: n

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

Missed letters: E A 
_ _ _ _ _ _ I _ N 

Guess a letter: o

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

Missed letters: E A 
_ _ O _ O _ I O N 

Guess a letter: t

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

Missed letters: E A 
_ _ O _ O T I O N 

Guess a letter: s

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========

Missed letters: E A S 
_ _ O _ O T I O N 

Guess a letter: l

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========

Missed letters: E A S L 
_ _ O _ O T I O N 

Guess a letter: m

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========

Missed letters: E A S L 
_ _ O M O T I O N 

Guess a letter: p

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========

Missed letters: E A S L 
P _ O M O T I O N 

Guess a letter: r
Yes! The secret word is "PROMOTION"! You have won!

Do you want to play again? 

```