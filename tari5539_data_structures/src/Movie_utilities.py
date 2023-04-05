"""
-------------------------------------------------------
Movie class utility functions.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 B
__updated__ = "2023-01-21"
-------------------------------------------------------
"""
from Movie import Movie


def get_movie():
    """
    -------------------------------------------------------
    Creates a Movie object by requesting data from a user.
    Use: movie = get_movie()
    -------------------------------------------------------
    Returns:
        movie - a Movie object based upon the user input (Movie).
    -------------------------------------------------------
    """

    # Your code here
    title = input("Title: ")
    year = int(input("Year of release: "))
    director = input("Director: ")
    rating = float(input("Rating: "))
    genres = read_genres()
    movie = Movie(title, year, director, rating, genres)
    return movie


def read_movie(line):
    """
    -------------------------------------------------------
    Creates and returns a Movie object from a line of formatted string data.
    Use: movie = read_movie(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of movie data in the format
          title|year|director|rating|genre codes (str)
    Returns:
        movie - a Movie object based upon the data from line (Movie)
    -------------------------------------------------------
    """

    # Your code here
    line = line.split("|")
    title = line[0]
    year = int(line[1])
    director = line[2]
    rating = float(line[3])
    gen = line[4].split(",")
    for i in range(0, len(gen)):
        gen[i] = int(gen[i])
    genres = gen
    movie = Movie(title, year, director, rating, genres)
    return movie


def read_movies(fv):
    """
    -------------------------------------------------------
    Reads a file of string data into a list of Movie objects.
    Use: movies = read_movies(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
    Returns:
        movies - a list of Movie objects (list of Movie)
    -------------------------------------------------------
    """

    # Your code here
    movies = []
    line = fv.readline()
    while line != "":
        # process line
        movie = read_movie(line)

        movies.append(movie)
        line = fv.readline()
    return movies


def read_genres():
    """
    -------------------------------------------------------
    Asks a user to select genres from a list of genres and returns
    an integer list of the genres chosen.
    Use: genres = read_genres()
    -------------------------------------------------------
    Returns:
        genres - sorted numeric list of movie genres (list of int)
    -------------------------------------------------------
    """

    # Your code here
    print(Movie.genres_menu())

    genres = []
    # new code
    print(Movie.genres_menu())
    x = input("Enter a genre number (ENTER to quit): ")
    # you only want it to stop when x is empty and there is at least 1 genre
    while not x == "" or len(genres) == 0:
        if not x.isnumeric() or int(x) < 0:  # checks if its not a number or if its bellow 0
            print("Error: not a positive number.")
        elif int(x) > 10:  # Checks if its bigger than 10
            print("Error: input must be <= 10")
        elif x in genres:  # checks if it already exists
            print("Error: genre already chosen")
        else:
            genres.append(x)
        x = input("Enter a genre number (ENTER to quit):")

    # turning to int from str
    for h in range(0, len(genres)):
        genres[h] = int(genres[h])
    genres.sort()

    return genres


def write_movies(fv, movies):
    """
    -------------------------------------------------------
    Writes the contents of movies to fv. Overwrites or
    creates a new file of Movie objects converted to strings.
    Use: write_movies(fv, movies)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
        movies - a list of Movie objects (list of Movie)
    Returns:
        None
    -------------------------------------------------------
    """

    # Your code here

    return


def get_by_year(movies, year):
    """
    -------------------------------------------------------
    Creates a list of Movies from a particular year.
    The original list of movies must be unchanged.
    Use: ymovies = get_by_year(movies, year)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        year - the Movie year to select (int)
    Returns:
        ymovies - Movie objects whose year attribute is
            year (list of Movie)
    -------------------------------------------------------
    """
    # Your code here
    ymovies = []

    for movie in movies:
        if movie.year == year:
            ymovies.append(movie)

    # alternatice method
    #ymovies = [movie for movie in movies if movie.year == year]
    return ymovies


def get_by_rating(movies, rating):
    """
    -------------------------------------------------------
    Creates a list of Movies whose ratings are equal to or higher
    than rating.
    The original list of movies must be unchanged.
    Use: rmovies = get_by_rating(movies, rating)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        rating - the minimum Movie rating to select (float)
    Returns:
        rmovies - Movie objects whose rating attribute is
            greater than or equal to rating (list of Movie)
    -------------------------------------------------------
    """
    # Your code here
    rmovies = []

    for movie in movies:
        if movie.rating >= rating:
            rmovies.append(movie)
    return rmovies


def get_by_genre(movies, genre):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include genre.
    The original list of movies must be unchanged.
    Use: gmovies = get_by_genre(movies, genre)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genre - the genre code to look for (int)
    Returns:
        gmovies - Movie objects whose genre list includes
            genre (list of Movie)
    -------------------------------------------------------
    """
    # Your code here
    gmovies = []
    for movie in movies:
        if genre in movie.genres:
            gmovies.append(movie)
    return gmovies


def get_by_genres(movies, genres):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include all the genre
    codes in genres.
    The original list of movies must be unchanged.
    Use: m = get_by_genres(movies, genres)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genres - the genre codes to look for (list of int)
    Returns:
        gmovies - Movie objects whose genre list includes
            all the genres in genres (list of Movie)
    -------------------------------------------------------
    """
    # Your code here
    gmovies = []
    for movie in movies:
        if genres == movie.genres:
            gmovies.append(movie)
    return gmovies


def genre_counts(movies):
    """
    -------------------------------------------------------
    Counts the number of movies in each genre given in Movie.GENRES.
    The original list of movies must be unchanged.
    Use: counts = genre_counts(movies)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
    Returns:
        counts - the number of Movies in each genre in Movie.GENRES.
            The index of each number in counts is the index of
            the matching genre in Movie.GENRES. (list of int)
    -------------------------------------------------------
    """
    # Your code here
    counts = [0]*11
    for movie in movies:
        if 0 in movie.genres:
            counts[0] += 1
        if 1 in movie.genres:
            counts[1] += 1
        if 2 in movie.genres:
            counts[2] += 1
        if 3 in movie.genres:
            counts[3] += 1
        if 4 in movie.genres:
            counts[4] += 1
        if 5 in movie.genres:
            counts[5] += 1
        if 6 in movie.genres:
            counts[6] += 1
        if 7 in movie.genres:
            counts[7] += 1
        if 8 in movie.genres:
            counts[8] += 1
        if 9 in movie.genres:
            counts[9] += 1
        if 10 in movie.genres:
            counts[10] += 1
    return counts
