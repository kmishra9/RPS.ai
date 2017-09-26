test = {
  'name': 'DetermineWinner',
  'points': 4,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def determine_winner_dummy(name, move, ai_move):
          ...   if move == ai_move:
          ...     return "Tie, no one wins!"
          ...   elif move == "rock" and ai_move == "scissors":
          ...     return name + " wins!"
          ...   elif move == "paper" and ai_move == "rock":
          ...     return name + " wins!"
          ...   elif move == "scissors" and ai_move == "paper":
          ...     return name + " wins!"
          ...   else:
          ...     return starter.determine_winner(name, scissor, rock)
          >>> name = 'urName'
          >>> rock = 'rock'
          >>> paper = 'paper'
          >>> scissor = 'scissors'
          >>> assert determine_winner_dummy(name, rock, scissor) == starter.determine_winner(name, rock, scissor), "step 4 1st case incorrect"
          >>> assert determine_winner_dummy(name, paper, rock) == starter.determine_winner(name, paper, rock), "step 4 2nd case incorrect"
          >>> assert determine_winner_dummy(name, scissor, paper) == starter.determine_winner(name, scissor, paper), "step 4 3rd case incorrect"
          >>> assert starter.determine_winner(name, scissor, rock) != ">>>>>>>>>>YOUR CODE HERE X<<<<<<<<<<", "step 4 losing case needs a unique message"
          >>> assert starter.determine_winner(name, scissor, rock) != "urName wins!", "step 4 losing case needs a unique message"
          >>> assert determine_winner_dummy(name, scissor, rock) == starter.determine_winner(name, scissor, rock), "step 4 losing case incorrect (or above cases are covering too many options"
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
      >>> import sys as sys
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
