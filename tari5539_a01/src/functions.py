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

# Constants

# task1


def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    newvals = []
    for x in values:
        if x not in newvals:
            newvals.append(x)
    values = newvals
    # print(values)

# task2


def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: u, l, d, w, r = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        u - the number of uppercase letters in the file (int)
        l - the number of lowercase letters in the file (int)
        d - the number of digits in the file (int)
        w - the number of whitespace characters in the file (int)
        r - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    u = 0
    l = 0
    d = 0
    w = 0
    r = 0
    line = fv.readline()
    while line != "":
        for i in range(0, len(line)):
            if line[i].isupper() is True:
                u += 1
            elif line[i].islower() is True:
                l += 1
            elif line[i].isdigit() is True:
                d += 1
            elif line[i] == " ":
                w += 1
            else:
                r += 1
        line = fv.readline()
    return u, l, d, w, r

# task3


def find_subs(string, sub):
    """
    -------------------------------------------------------
    Finds the indices of the locations of sub within string,
        left to right.
    Use: locations = find_subs(string, sub)
    -------------------------------------------------------
    Parameters:
        string - a string to evaluate (str)
        sub - a substring to locate in string (str)
    Returns:
        locations - an ordered list of the indices of the locations
            of sub within string (list of int)
    -------------------------------------------------------
    """
    locations = []
    for i in range(0, len(string)):
        if sub in string[i:i+len(sub)]:
            locations.append(i)
    return locations

# task4


def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """
    leap_year = False
    if year % 100 == 0 and year % 400 != 0:
        leap_year = False
    elif year % 400 == 0 or year % 4 == 0:
        leap_year = True
    return leap_year
# task5


def is_valid(name):
    """
    -------------------------------------------------------
    Determines if name is a valid Python variable name.
    Variables names must start with a letter or an underscore.
    The rest of the variable name may consist of letters, numbers
    and underscores.
    Use: valid = is_valid(name)
    -------------------------------------------------------
    Parameters:
        name - a string to test as a Python variable name (str)
    Returns:
        valid - True if name is a valid Python variable name,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    valid = True
    if name[0].isalpha() is False and name[0] != "_":
        valid = False

    for i in range(1, len(name)):
        if name[i].isalpha() is False and name[i].isdigit() is False:
            valid = False
    return valid
# task6


def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """

    rows = len(a)
    cols = len(a[0])
    b = []
    for i in range(0, cols):

        row = []
        for item in a:

            row.append(item[i])
        b.append(row)

    return b

# task7


def matrixes_multiply(a, b):
    """
    -------------------------------------------------------
    Multiplies the contents of matrixes a and b.
    If a is mxn in size, and b is nxp in size, then c is mxp.
    a and b must be unchanged.
    Use: c = matrixes_multiply(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix multiple of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    c = []
    rows = len(a)
    cols = len(b[0])
    c1 = len(a[0])
    c = [[0]*cols]*rows
    for i in range(0, rows):
        for j in range(0, cols):
            c[i][j] = 0
            for k in range(0, c1):
                c[i][j] = c[i][j] + a[i][k] * b[k][j]
    return c
# task8


def pig_latin(word):
    """
    -------------------------------------------------------
    Converts a word to Pig Latin. The conversion is:
    - if a word begins with a vowel, add "way" to the end of the word.
    - if the word begins with consonants, move the leading consonants to
    the end of the word and add "ay" to the end of that.
    "y" is treated as a consonant if it is the first character in the word,
    and as a vowel for anywhere else in the word.
    Preserve the case of the word - i.e. if the first character of word
    is upper-case, then the new first character should also be upper case.
    Use: pl = pig_latin(word)
    -------------------------------------------------------
    Parameters:
        word - a string to convert to Pig Latin (str)
    Returns:
        pl - the Pig Latin version of word (str)
    ------------------------------------------------------
    """
    pl = ''
    vowels = ["a", "e", "o", "i", "u"]
    vowels2 = ["a", "e", "o", "i", "u", "y"]
    caps = word[0].isupper()  # cehcks caps of first letter
    # for vowels
    if word[0].lower() in vowels:
        word = word + "way"
    # for consonants
    elif word[0].lower() not in vowels:
        i = 0
        vowelfound = ""
        subnum = 0
        while i < len(word)-1 or vowelfound == False:
            if word[i+1] in vowels2 is True:
                vowelfound == True
                subnum = i
            i += 1
        sub = word[0:2+subnum]
        word = word[2+subnum:]
        word = word + sub
        word = word + "ay"

    pl = word
    return pl
# task9


def shift(string, n):
    """
    -------------------------------------------------------
    Encipher a string using a shift cipher.
    Only letters are enciphered, and the returned string is
    in upper case.
    Use: estring = shift(string, n):
    -------------------------------------------------------
    Parameters:
        string - string to encipher (str)
        n - the number of letters to shift (int)
    Returns:
        estring - the enciphered string (str)
    -------------------------------------------------------
    """
    estring = ""
    LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    string = string.upper()
    for x in range(0, len(string)):
        if string[x].isalpha() is True:
            index = LETTERS.index(string[x])
            if index + n > 25:
                newindex = index + n - 26
                estring = estring + LETTERS[newindex]
            elif index + n < 0:
                newindex = 26 - (index + n)
                estring = estring + LETTERS[newindex]
            else:
                estring = estring + LETTERS[index+n]
        else:
            estring = estring + string[x]

    return estring
