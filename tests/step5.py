test = {
  'name': 'Main',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> starter.main()
          Enter your name:
          Enter your move: (rock, paper, or scissors)
          name plays rock
          AI plays rock
          Tie, no one wins!
          Do you want to play again? (yes or no)
          >>> starter.main()
          Enter your name:
          Enter your move: (rock, paper, or scissors)
          name plays scissors
          AI plays rock
          AI wins!
          Do you want to play again? (yes or no)
          Enter your move: (rock, paper, or scissors)
          name plays paper
          AI plays rock
          name wins!
          Do you want to play again? (yes or no)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'setup': r"""
      >>> import os as os
      >>> import subprocess as subprocess
      >>> import starter_RPS as starter
      >>> import sys as sys #Try redefining starter play and play_again
      >>> count = 0
      >>> def input(prompt=""):
      ...   if prompt != "": print(prompt)
      ...   test_inputs = ["name", "rock", "no", "name", "scissors", "yes", "paper", "no"]
      ...   global count
      ...   count += 1
      ...   return test_inputs[count - 1]
      >>> starter.input = input
      >>> def rock_ai():
      ...   moves = ["rock"]
      ...   return moves[0]
      >>> def play(name, ai=rock_ai, silent=False):
      ...   prompt = "Enter your move: (rock, paper, or scissors) "
      ...   print(prompt)
      ...   move = input()
      ...   move = move.lower()
      ...   ai_move = ai()
      ...   winner = determine_winner(name, move, ai_move)
      ...   if silent == False:
      ...     print(name + " plays " + move)
      ...     print("AI plays " + ai_move)
      ...     print(winner)
      ...   return winner
      >>> def play_again():
      ...     prompt = "Do you want to play again? (yes or no) "
      ...     print(prompt)
      ...     choice = input()
      ...     choice = choice.lower()
      ...     if choice == "yes":
      ...         return True
      ...     elif choice == "no":
      ...         return False
      ...     else:
      ...         print("Invalid input!\n")
      ...         return play_again()
      >>> def determine_winner(name, move, ai_move):
      ...     assert ( (move    == "rock" or move    == "paper" or move    == "scissors") and
      ...            (ai_move == "rock" or ai_move == "paper" or ai_move == "scissors")
      ...           ), "Wrong move or ai_move argument passed in"
      ...     if move == ai_move:
      ...         return "Tie, no one wins!"
      ...     elif move == "rock" and ai_move == "scissors":
      ...         return name + " wins!"
      ...     elif move == "paper" and ai_move == "rock":
      ...         return name + " wins!"
      ...     elif move == "scissors" and ai_move == "paper":
      ...         return name + " wins!"
      ...     else:
      ...         return "AI wins!"
      >>> starter.play_again = play_again
      >>> starter.play = play
      >>> starter.determine_winner = determine_winner
      >>> real_print = print
      >>> def print(string):
      ...   real_print(string.strip())
      >>> starter.print = print
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
