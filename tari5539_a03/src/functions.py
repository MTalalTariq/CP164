"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-02-01"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from enum import Enum
# Constants
OPERATORS = "+-*/"  # for postfix(string)


def stack_split_alt(source):  # task1
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    target1 = Stack()
    target2 = Stack()
    i = 1
    while source.is_empty() is False:
        if i % 2 != 0:
            target1.push(source.pop())
        else:
            target2.push(source.pop())
        i += 1
    return target1, target2


def is_palindrome_stack(string):  # task3
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    palindrome = False
    stringarr = []
    string = string.lower()
    # turn string into array
    for i in string:
        if i.isalpha() is True:
            stringarr.append(i.lower())
    # print(stringarr)
    # make sure its not 1 or 0 length string
    if len(stringarr) == 1 or len(stringarr) == 0:
        palindrome = True
    # remove middle letter if length if string is odd
    elif len(stringarr) % 2 != 0:
        # print("odd")
        middle = int((len(stringarr) - 1)/2)
        del stringarr[middle]
    # print(stringarr)
    # put each half into two stacks
    fhalf = Stack()
    shalf = Stack()
    # first half
    half = int(len(stringarr)/2)
    for i in range(0, half, 1):
        fhalf.push(stringarr[i])
    # second half, backwards
    for i in range(len(stringarr)-1, half - 1, -1):
        shalf.push(stringarr[i])
    # print(fhalf._values)
    # print(shalf._values)
    possiblepalin = True
    for i in range(0, half, 1):
        if shalf.pop() != fhalf.pop():
            possiblepalin = False
    if possiblepalin is True:
        palindrome = True
    return palindrome


def postfix(string):  # task4
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    s = Stack()
    string = string.split()
    # print(string)
    for i in string:
        if i.isdigit() is True:  # if its a digit
            s.push(float(i))
        elif i in OPERATORS:  # if its an operator
            op = OPERATORS.index(i)
            pop1 = s.pop()
            pop2 = s.pop()
            if op == 0:  # addition
                result = pop2 + pop1
                s.push(result)
            elif op == 1:  # subtraction
                result = pop2 - pop1
                s.push(result)
            elif op == 2:  # multiply
                result = pop2 * pop1
                s.push(result)
            elif op == 3:  # divide
                result = pop2 / pop1
                s.push(result)
    answer = s.pop()
    return answer


def stack_maze(maze):  # task5
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            None if there is no exit (list of str)
    -------------------------------------------------------
    """
    path = []
    s = Stack()
    key = 'Start'

    while key != "X":
        # alphabetically organizing list for optimal solution
        maze[key].sort()
        # putting all the available options in stack
        for i in maze[key]:
            s.push(i)
            # print(s._values)

        # stack will be empty if there is no end
        # meaning it backtracked to to the beginning w no other options
        if s.is_empty() is True:
            path = None
            break

        # taking the next path
        key = s.pop()
        # adding our route to the path var
        path.append(key)
        # print(s._values)
    return path


# Enumerated constant
MIRRORED = Enum('MIRRORED',
                {'IS_MIRRORED': "is a mirror", 'TOO_MANY_LEFT': "too many characters in L",
                 'TOO_MANY_RIGHT': "too many characters in R", 'MISMATCHED': "L and R don't match",
                 'INVALID_CHAR': "invalid character", 'NOT_MIRRORED': "no mirror character"})


def is_mirror_stack(string, valid_chars, m):  # task6
    """
    -------------------------------------------------------
    Determines if string is a mirror of characters in valid_chars around the pivot m.
    A mirror is of the form LmR, where L is the reverse of R, and L and R
    contain only characters in valid_chars.
    Use: mirror = is_mirror_stack(string, valid_chars, m)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
        valid_chars - a string of valid characters (str)
        m - the mirror pivot string (str - one character not in valid_chars)
    Returns:
        mirror - the state of the string (Enum MIRRORED)
    -------------------------------------------------------
    """
    assert m not in valid_chars, \
        f"cannot use '{m}' as the mirror character"

    mirror = MIRRORED.IS_MIRRORED
    stack = Stack()
    n = len(string)
    i = 0
    # working with L
    while i < n and string[i] != m and mirror == MIRRORED.IS_MIRRORED:
        if string[i] in valid_chars:
            stack.push(string[i])
            i += 1
        else:
            #mirror = False
            mirror = MIRRORED.INVALID_CHAR
    lenofl = i
    if m not in string:
        #print("no m")
        mirror = MIRRORED.NOT_MIRRORED

    # skip over the mirror character
    i += 1

    while (mirror == MIRRORED.IS_MIRRORED) and i < n and not stack.is_empty():
        c = stack.pop()

        if string[i] != c:
            #mirror = False
            mirror = MIRRORED.MISMATCHED
        else:
            i += 1

    # checking length of each side
    lenofr = len(string) - lenofl - 1
    #print(lenofl, lenofr, len(string))
    if mirror == MIRRORED.IS_MIRRORED:
        if lenofr > lenofl:
            mirror = MIRRORED.TOO_MANY_RIGHT
        if lenofl > lenofr:
            mirror = MIRRORED.TOO_MANY_LEFT

    "not (i == n and stack.is_empty())"
    "i != n and stack.is_empty() is False"
    # check final conditions
    if not (i == n and stack.is_empty()) and mirror == MIRRORED.IS_MIRRORED:
        mirror = False

    return mirror
