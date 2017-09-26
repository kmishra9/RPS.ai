test = {
  'name': 'BasicAI',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> expected = 9
          >>> outputs = ["rock", "paper", "scissors"]
          >>> rcount = 0
          >>> scount = 0
          >>> pcount = 0
          >>> for i in range(2*expected):
          ...   move = starter.basic_ai()
          ...   assert move in outputs, "Step 2 returns the wrong output"
          ...   if (move == "rock"):
          ...     rcount += 1
          ...   if (move == "scissors"):
          ...     scount += 1
          ...   if (move == "paper"):
          ...     pcount += 1
          >>> assert rcount > 0, " You seem to be getting a low number of rocks"
          >>> assert scount > 0, " You seem to be getting a low number of scissors"
          >>> assert pcount > 0, " You seem to be getting a low number of papers"
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
