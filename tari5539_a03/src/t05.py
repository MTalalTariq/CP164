"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-02-05"
-------------------------------------------------------
"""
# Imports
from functions import stack_maze
# Constants

maze1 = {'Start': ['A'],
         'A': ['B', 'C'],
         'B': [],
         'C': ['D', 'E'],
         'D': [],
         'E': ['F', 'X'],
         'F': ['G', 'H'],
         'G': [],
         'H': []}
# maze1 reverse
maze1r = {'Start': ['A'],
          'A': ['C', 'B'],
          'B': [],
          'C': ['E', 'D'],
          'D': [],
          'E': ['X', 'F'],
          'F': ['H', 'G'],
          'G': [],
          'H': []}

# circular maze
maze2 = {'Start': ['A'],
         'A': ['B', 'C'],
         'B': [],
         'C': ['D', 'E'],
         'D': [],
         'E': ['X', 'F'],
         'F': ['G'],
         'G': ['C']}

# circular maze reverse
maze2r = {'Start': ['A'],
          'A': ['C', 'B'],
          'B': [],
          'C': ['E', 'D'],
          'D': [],
          'E': ['F', 'X'],
          'F': ['G'],
          'G': ['C']}

# no end
maze3 = {'Start': ['A'],
         'A': []}

path = stack_maze(maze2)
print("path is", path)
