"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-01-14"
-------------------------------------------------------
"""
# Imports
from Movie import Movie
# Constants

m2 = Movie('T2', 2000, 'D2', 5, [0, 1, 3, 9])
string = m2.genres_list_string()
print(string)
