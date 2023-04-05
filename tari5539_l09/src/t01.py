"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-03-23"
-------------------------------------------------------
"""
# Imports
from functions import hash_table
from Movie import Movie
# Constants


slots = 7
m1 = Movie("Dark City", 1998, None, None, None)
m2 = Movie("Zulu", 1964, None, None, None)
m3 = Movie("I Am Legend", 2007, None, None, None)
m4 = Movie("Omega Man, The", 1971, None, None, None)
values = [m1, m2, m3, m4]

hash_table(slots, values)
