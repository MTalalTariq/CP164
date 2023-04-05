"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-01-17"
-------------------------------------------------------
"""
# Imports
from Movie import Movie


# Constants

avater = Movie('Avater', 2009, 'james', 8.8, [0, 1, 3, 9])
string = avater.genres_string()
print(string)
