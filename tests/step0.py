test = {
  'name': 'GetName',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> starter.get_name()
          Enter your name:
          'name'
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
      ...   if prompt != "": print(prompt.strip())
      ...   test_inputs = ["name"]
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
