## Blackjack
A command-line implementation of the classic casino card game Blackjack (also known as 21) written in Python.

As I am becoming more comfortable with using Python, I am exploring and challenging myself to code different games in Python.

### Getting started

You will need:
- Python 3.6 or higher installed on your system
- Clone this repository to your local machine:
`git clone https://github.com/yourusername/blackjack-game.git
cd blackjack-game`
- To play the game you need to run: python3 blackjack.py
- To run the tests: `python3 -m unittest discover test`

### Description

This Blackjack game allows players to compete against a dealer using standard playing card rules. The objective is to beat the dealer by getting a hand value as close to 21 as possible without going over.

### How to play

The game will deal two cards to you and two to the dealer (one face-up, one face-down)
Choose to either:

- Hit (receive another card)
Stand (keep your current hand)

Continue making decisions until you either:

- Stand with a hand you're satisfied with
- Bust (go over 21)
- Get Blackjack

### Future improvements

* Add support for multiple players
* * Implement betting system
Add option for splitting pairs



