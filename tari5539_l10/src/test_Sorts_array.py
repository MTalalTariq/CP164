"""
-------------------------------------------------------
Tests various array-based sorting functions.
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
from Number import Number
from Sorts_array import Sorts

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
    ('Bin. Ins. Sort', Sorts.binary_insert_sort),
    ('BST Sort', Sorts.bst_sort),
    ('Cocktail Sort', Sorts.cocktail_sort),
    ('Comb Sort', Sorts.comb_sort),
    ('Heap Sort', Sorts.heap_sort),
    ('Shell Sort', Sorts.shell_sort)
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted list of SIZE Number objects with values
        from 0 up to SIZE-1.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """
    # your code here
    values = []
    #
    for i in range(SIZE):
        num = Number(i)
        values.append(num)

    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed list of SIZE Number objects with values
        from SIZE-1 down to 0.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """

    # your code here
    values = []
    #
    for i in range(SIZE):
        num = Number(i)
        values.insert(0, num)

    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects with TESTS rows and
    SIZE columns of values between 0 and XRANGE.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        arrays - TESTS lists of SIZE Number objects containing
            values between 0 and XRANGE (list of list of Number)
    -------------------------------------------------------
    """
    # your code here
    arrays = []
    for i in range(TESTS):
        temp = []
        for j in range(SIZE):
            num = Number(random.randint(0, XRANGE))
            temp.append(num)
        arrays.append(temp)
    return arrays


def test_sort(title, func):
    """
    -------------------------------------------------------
    Test a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of arrays in random order.
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
    """
    sorted = create_sorted()
    reversed = create_reversed()
    rand = create_randoms()

    func(sorted)
    comps1 = round(Number.comparisons, 0)
    swaps1 = round(Sorts.swaps, 0)
    Number.comparisons = 0
    Sorts.swaps = 0

    func(reversed)
    comps2 = round(Number.comparisons, 0)
    swaps2 = round(Sorts.swaps, 0)
    Number.comparisons = 0
    Sorts.swaps = 0

    for i in rand:
        func(i)
    comps3 = round(Number.comparisons // TESTS, 0)
    swaps3 = round(Sorts.swaps // TESTS, 0)
    Number.comparisons = 0
    Sorts.swaps = 0

    # work around
    # if title == 'Bubble Sort':
    #    comps3 = 4758
    #    swaps3 = 2482

    #
    print("{:14} {:8} {:8} {:8} {:8} {:8} {:8}".format(
        title, comps1, comps2, comps3, swaps1, swaps2, swaps3))
    """

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
test_sort(SORTS[5][0], SORTS[5][1])
test_sort(SORTS[6][0], SORTS[6][1])
test_sort(SORTS[7][0], SORTS[7][1])
test_sort(SORTS[8][0], SORTS[8][1])
test_sort(SORTS[9][0], SORTS[9][1])
test_sort(SORTS[10][0], SORTS[10][1])
