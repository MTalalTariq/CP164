"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-01-21"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from Movie import Movie
from utilities import stack_test
# Constants

# getting objects from txt file and putting into list
source = []
fh = open("movies.txt", "r", encoding="utf-8")
line = fh.readline()
while line != "":
    line = line.split("|")
    title = line[0]
    year = int(line[1])
    director = line[2]
    rating = float(line[3])
    genres = []
    genresstring = line[4].split(",")
    for i in range(0, len(genresstring)):
        genres.append(int(genresstring[i]))
    m1 = Movie(title, year, director, rating, genres)
    source.append(m1)
    line = fh.readline()
fh.close()

stack_test(source)
