"""
-------------------------------------------------------
Tests various linked sorting functions.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 C
__updated__ = "2023-03-30"
-------------------------------------------------------
"""
# Imports
import random

from List_linked import List
from Number import Number
from Sorts_List_linked import Sorts

# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted List of Number objects.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """

    # your code here
    values = List()
    for i in range(SIZE):
        temp_num = Number(i)
        values.append(temp_num)
    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed List of Number objects.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """

    # your code here
    values = List()
    for i in range(SIZE-1, -1, -1):
        temp_num = Number(i)
        values.append(temp_num)

    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects with TESTS rows and
    SIZE columns of values between 0 and XRANGE.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        lists - TESTS lists of SIZE Number objects containing
            values between 0 and XRANGE (list of List of Number)
    -------------------------------------------------------
    """

    # your code here
    lists = []
    for i in range(TESTS):
        temp = List()
        for j in range(SIZE):
            temp.append(Number(random.randint(0, XRANGE)))

        lists.append(temp)

    return lists


def test_sort(title, func):
    """
    -------------------------------------------------------
    Tests a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of Lists in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """

    # your code here
    random = create_randoms()
    random_c = 0
    spacing = " " * (15 - len(title))

    Number.comparisons = 0
    Sorts.swaps = 0

    print(f"{title:>s}", end='')
    func(create_sorted())
    sorted_c = Number.comparisons
    swaps_sorted = Sorts.swaps

    Number.comparisons = 0
    Sorts.swaps = 0

    func(create_reversed())
    reversed_c = Number.comparisons
    swaps_reversed = Sorts.swaps

    Number.comparisons = 0
    Sorts.swaps = 0

    for i in random:
        func(i)
        random_c += Number.comparisons
        Number.comparisons = 0
    random_c = random_c / len(random)
    swaps_random = Sorts.swaps / len(random)

    print(f"{spacing} {sorted_c:^8.0f} {reversed_c:^8.0f} {random_c:^8.0f} {swaps_sorted:^8.0f}         {swaps_reversed:^8.0f}         {swaps_random:>8.0f}")

    return


# testing
print("n:   100       |      Comparisons       | |         Swaps          |")
print("Algorithm      In Order Reversed   Random In Order Reversed   Random")
print("-------------- -------- -------- -------- -------- -------- --------")

test_sort(SORTS[0][0], SORTS[0][1])
test_sort(SORTS[1][0], SORTS[1][1])
test_sort(SORTS[2][0], SORTS[2][1])
test_sort(SORTS[3][0], SORTS[3][1])
test_sort(SORTS[4][0], SORTS[4][1])
