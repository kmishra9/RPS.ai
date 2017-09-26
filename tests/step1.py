test = {
  'name': 'PlayAgain',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert starter.play_again() == True, 'check standard input'
          Do you want to play again? (yes or no)
          >>> assert starter.play_again() == False, 'check standard input'
          Do you want to play again? (yes or no)
          >>> assert starter.play_again() == True, 'check uppercase input'
          Do you want to play again? (yes or no)
          >>> assert starter.play_again() == False, 'check uppercase input'
          Do you want to play again? (yes or no)
          >>> assert starter.play_again() == False, 'check the third case'
          Do you want to play again? (yes or no)
          Invalid input!
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
      >>> import sys as sys
      >>> real_print = print
      >>> def print(string):
      ...   real_print(string.strip())
      >>> starter.print = print
      >>> count = 0
      >>> def input(prompt=""):
      ...   if prompt != "": print(prompt)
      ...   test_inputs = ["yes", "no", "YES", "nO", "blah", "No"]
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
