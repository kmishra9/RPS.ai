"""
    RPS STARTER Code

	main: starts the game and begins play, also has a section for taking in choice.
	play: plays the game by finding a move for player and ai_player and then comparing them in
			determine_winner and saying the winner.
    play_again: takes in the choice of the player and decides whether or not the player wants to
            play again.
	ai_player: returns a move for the AI player
	determine_winner: takes in two moves, and then determines who wins
"""

import random

"""Controls playing"""
def play(name):
    #Your Code Here
    return None

"""Checks if they want to play again"""
def play_again(choice):
    #Your Code Here
    return None

"""Simply returns a random move from list. """
def ai_player():
    #Replace code here
    moves = [1, 2, 3]
    move = random.randint(0, 100)
    return moves[move];

"""Determines winner of the current battle."""
def determine_winner(name, move, ai_move):
    if move == ai_move:
        return "Tie, no one wins!"
    if move == "rock" and ai_move == "scissors":
        return name + " wins!"
    #Your Code Here
    return None

"""Runs program and continues playing while play returns true."""
def main():
    #Your Code Here
    playing = True
    while (playing):
        play(name)
        #Your Code Here Should only be one line (Check below for clues)
        playing = play_again(choice)

if __name__ == "__main__":
    main()
