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
from Movie_utilities import get_by_genres
# Constants

movies = []
m1 = Movie('T1', 2000, 'D1', 5, [3, 4])
m2 = Movie('T2', 2001, 'D2', 5.5, [3, 4, 5])
m3 = Movie('T3', 2000, 'D3', 6, [3])
m4 = Movie('T4', 2001, 'D4', 9.8, [3, 4])
movies = [m1, m2, m3, m4]
genres = [3, 4]

m = get_by_genres(movies, genres)

for movie in m:
    print(movie.title)
