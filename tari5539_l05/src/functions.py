"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-02-13"
-------------------------------------------------------
"""
# Imports

# Constants


def recurse(x, y):  # task1
    """
    -------------------------------------------------------
    Recursive function - example of tree recursion.
    Use: ans = recurse(x, y)
    -------------------------------------------------------
    Parameters:
        x - an integer (int)
        y - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    if x < 0 or y < 0:  # base case
        ans = x-y
    else:  # general case
        ans = recurse(x-1, y) + recurse(x, y-1)
    return ans


def gcd(m, n):  # task2
    """
    -------------------------------------------------------
    Recursively find the Greatest Common Denominator of two numbers.
    Use: ans = gcd(m, n)
    -------------------------------------------------------
    Parameters:
        n - an integer (int)
        m - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    if m % n == 0:  # base case
        ans = n
    else:  # general case
        ans = gcd(n, m % n)
    return ans


def vowel_count(s):  # task3
    """
    -------------------------------------------------------
    Recursively counts number of vowels in a string.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - string to examine (str)
    Returns:
        count - number of vowels in s (int)
    -------------------------------------------------------
    """
    VOWELS = "aeiou"
    if s == "":  # base case
        count = 0
    elif s[0].lower() in VOWELS and s[0].isalpha():  # general case: vowel
        count = 1 + vowel_count(s[1:])
    else:  # general case: no vowel
        count = vowel_count(s[1:])
    return count


def to_power(base, power):  # task 4
    """
    -------------------------------------------------------
    Calculates base^power.
    Use: ans = to_power(base, power)
    -------------------------------------------------------
    Parameters:
        base - base to apply power to (float)
        power - power to apply (int)
    Returns:
        ans - base ^ power (float)
    -------------------------------------------------------
    """
    if power == 0:  # base case
        ans = 1
    elif power > 0:  # general case: positive power
        ans = to_power(base, power-1)*base
    else:  # general case: negative power
        ans = to_power(base, power+1) / base
    return ans


def is_palindrome(s):  # task5
    """
    -------------------------------------------------------
    Recursively determines if s is a palindrome. Ignores non-letters and case.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    palindrome = True
    if len(s) == 0 or len(s) == 1:  # base case
        palindrome = True
    # general case: left character is alpha but right side is not
    elif s[0].isalpha() and not s[-1].isalpha():
        palindrome = is_palindrome(s[:-1])
    # general case: left character is not alpha but right side is
    elif not s[0].isalpha() and s[-1].isalpha():
        palindrome = is_palindrome(s[1:])
    # general case: left and right character is not alpha
    elif not s[0].isalpha() and not s[-1].isalpha():
        palindrome = is_palindrome(s[1:-1])
    else:  # general case: left and right character is alpha
        # more general cases

        # general case: if they dont equal eachother(recursion ends)
        # also a base case as it ends the recursion
        if s[0].lower() != s[-1].lower():
            palindrome = palindrome = False
        else:  # general case: if they equal eachother
            palindrome = is_palindrome(s[1:-1])
    return palindrome


def bag_to_set(bag):  # task6
    """
    -------------------------------------------------------
    Copies elements of a bag to a set.
    Use: new_set = bag_to_set(bag)
    -------------------------------------------------------
    Parameters:
        bag - a list of values (list)
    Returns:
        new_set - containing one each of the elements in bag (list)
    -------------------------------------------------------
    """
    """ old
    if not bag:  # base case
        new_set = []
    elif bag[0] not in new_set:  # general case: new value
        new_set = [bag[0]] + bag_to_set(bag[1:])
    else:  # general case: repeated value
        new_set = bag_to_set(bag[1:])
    """
    """ old #2
    if not bag:
        new_set = []

    elif bag[-1] in bag[:-1]:
        print(bag, "s1")
        new_set = bag_to_set(bag[:-1])

    elif bag[0] in bag[1:]:
        print(bag, "s2")
        new_set = bag_to_set(bag[:-1])

    else:
        print(bag, "s3")
        new_set = [bag[0]] + bag_to_set(bag[1:])
    """
    if not bag:  # base case
        new_set = []
    elif bag[-1] in bag[:-1]:  # general case #1: remove from end
        #print(bag, "remove from end", bag[-1])
        new_set = bag_to_set(bag[:-1])  # general case #2: remove 2nd last
    elif len(bag) > 1 and bag[-2] in bag[:-2]:
        #print(bag, "remove from near end", bag[-2])
        new_set = bag_to_set(bag[:-2]+[bag[-1]])
    else:  # general case #3: add to new_set
        #print(bag, "add front", bag[0])
        new_set = [bag[0]] + bag_to_set(bag[1:])
    return new_set
