test = {
  'name': 'Play',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def rock_ai():
          ...   moves = ["rock"]
          ...   return moves[0]
          >>> starter.play('name', rock_ai)
          Enter your move: (rock, paper, or scissors) 
          name plays rock
          AI plays rock
          Tie, no one wins!
          'Tie, no one wins!'
          >>> starter.play('name', rock_ai)
          Enter your move: (rock, paper, or scissors) 
          name plays scissors
          AI plays rock
          AI wins!
          'AI wins!'
          >>> starter.play('name', rock_ai, True) #check that silent mode works correctly
          Enter your move: (rock, paper, or scissors) 
          'name wins!'
          >>> starter.play('name', rock_ai, True) #check that your input is properly formatted
          Enter your move: (rock, paper, or scissors) 
          'Tie, no one wins!'
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
      >>> count = 0
      >>> def input(prompt=""):
      ...   if prompt != "": print(prompt)
      ...   test_inputs = ["rock", "scissors", "paper", "ROCK"]
      ...   global count
      ...   count += 1
      ...   return test_inputs[count - 1]
      >>> starter.input = input
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
