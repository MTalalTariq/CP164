"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-01-15"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import read_movies
# Constants

fv = open("movies.txt", "r", encoding="utf-8")
"""
line = fh.readline()
while line != "":
    # process line
    movie = read_movie(line)
    line = fh.readline()
"""
movies = read_movies(fv)
fv.close()
