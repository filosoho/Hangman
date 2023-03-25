# Hangman Game

This is a simple Hangman game developed in Python. 

The game selects a random word from a list and prompts the user to guess letters in the word. The user has 6 lives to guess all the letters in the word. If the user runs out of lives before guessing the word, they lose the game. If the user guesses all the letters in the word before running out of lives, they win.

# How to Play:

Clone this repository to your local machine.
Open the terminal or command prompt and navigate to the cloned repository directory.

Run the following command to start the game:

```
main.py
```

The game will prompt you to guess a letter. Type in a letter and press Enter.
The game will display the word with the correctly guessed letters filled in and underscores for the remaining letters.
Keep guessing letters until you either guess the whole word or run out of lives.

Good luck and have fun!

~~~  
  _                                            
 | |                                           
 | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
 | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | | | | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/                       

Welcome to Hangman!

_ _ _ _ _ _ _ _ 

Guess a letter: a
--------------------------------------------------------------
The letter 'a' is not in this word. You loose a life.
--------------------------------------------------------------
 
  +---+
  |   |
  O   |
      |
      |
      |
=========
_ _ _ _ _ _ _ _ 

Guess a letter: e

e _ _ _ e _ _ _ 

Guess a letter: i
--------------------------------------------------------------
The letter 'i' is not in this word. You loose a life.
--------------------------------------------------------------
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
e _ _ _ e _ _ _ 

Guess a letter: o

e _ _ o e _ _ _ 

Guess a letter: u
--------------------------------------------------------------
The letter 'u' is not in this word. You loose a life.
--------------------------------------------------------------
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
e _ _ o e _ _ _ 

Guess a letter: s
--------------------------------------------------------------
The letter 's' is not in this word. You loose a life.
--------------------------------------------------------------
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
e _ _ o e _ _ _ 

Guess a letter: t

e _ _ o e t _ _ 

Guess a letter: r

e _ _ o e t _ r 

Guess a letter: n
--------------------------------------------------------------
The letter 'n' is not in this word. You loose a life.
--------------------------------------------------------------
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
e _ _ o e t _ r 

Guess a letter: l

e _ _ o e t l r 

Guess a letter: m
--------------------------------------------------------------
The letter 'm' is not in this word. You loose a life.
--------------------------------------------------------------
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
e _ _ o e t l r 

You lose.

====================================

The word was seashell

====================================
~~~  


# Contributing

If you would like to contribute to this program, feel free to submit a pull request. Please include a detailed description of the changes made and the reasons for the changes.

# License

Feel free to use and modify the code as per your requirements.
