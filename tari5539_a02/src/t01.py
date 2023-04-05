"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-01-20"
-------------------------------------------------------
"""
# Imports
from Movie import Movie
from Movie_utilities import get_by_year
# Constants

movies = []
m1 = Movie('T1', 2000, 'D1', 5, [0, 1, 3, 9])
m2 = Movie('T2', 2001, 'D2', 9, [0, 4, 7])
m3 = Movie('T3', 2000, 'D3', 5.4, [8, 9])
m4 = Movie('T4', 2001, 'D4', 8, [0, 5, 7])
movies = [m1, m2, m3, m4]
year = int(input("year: "))

# for movie in movies:
#   print(movie.title)

ymovies = get_by_year(movies, year)

for movie in ymovies:
    print(movie.title)
