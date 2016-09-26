"""
    RPS STAFF SOLUTION
	main: starts the game and begins play
	play: plays the game by finding a move for player and ai_player and then comparing them in
			determine_winner and then asking if the player wants to play again.
	ai_player: returns a move for the AI player
	determine_winner: takes in two moves, and then determines who wins
"""

import random


"""Plays and then prints the winner"""
def play(name):
    print("You have 3 choices, Rock, Paper, or Scissors.")
    move = input("Enter your choice (rock, paper, scissors): ")
    move = move.lower()
    ai_move = ai_player()
    print(name + " plays " + move)
    print("AI plays " + ai_move)
    win = determine_winner(name, move, ai_move)
    print(win)

"""Checks if they want to play again"""
def play_again(choice):
    choice = choice.lower()
    if choice == "yes":
        return True
    elif choice == "no":
        return False

"""Simply returns a random move from list. """
def ai_player():
    moves = ["rock", "paper", "scissors"]
    move = random.randint(0, 2)
    return moves[move];

"""Determines winner of the current battle."""
def determine_winner(name, move, ai_move):
    if move == ai_move:
        return "Tie, no one wins!"
    if move == "rock" and ai_move == "scissors":
        return name + " wins!"
    elif move == "scissors" and ai_move == "paper":
        return name + " wins!"
    elif move == "paper" and ai_move == "rock":
        return name + " wins!"
    elif move == "rock" and ai_move == "paper":
        return "AI Player wins!"
    elif move == "scissors" and ai_move == "rock":
        return "AI Player wins!"
    elif move == "paper" and ai_move == "scissors":
        return "AI Player wins!"

"""Runs program and continues playing while play returns true."""
def main():
    name = input("Enter your name: ")
    print("Hi " + name + "!" + " Welcome to Rock Paper Scissors!")
    playing = True
    while (playing):
        play(name)
        choice = input("Do you want to play again (yes, no)? ")
        playing = play_again(choice)

if __name__ == "__main__":
    main()
