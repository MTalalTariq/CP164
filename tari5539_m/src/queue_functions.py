"""
-------------------------------------------------------
Midterm Queue Functions
-------------------------------------------------------
Author: Talal Tariq
ID:     169035539
Email:  tari5539@mylaurier.ca
__updated__ = "2023-03-04"
-------------------------------------------------------
"""


def queue_rotate(source, n):
    """
    -------------------------------------------------------
    Rotates position of values in source. When finished, values
    in source are rotated n positions to the right.
    Use: queue_rotate(source, n)
    -------------------------------------------------------
    Parameters:
        source - the Queue to rotate (Queue)
        n - amount to rotate Queue values (int)
    Returns‌​‌​​​​‌​​‌‌​‌​​​‌‌‌​​​‌​​‌‌:
        None
    -------------------------------------------------------
    """

    # Your code here
    if n > 0:
        i = 0
        while i < n:
            num = source.remove()
            source.insert(num)
            i += 1
    if n < 0:
        n = n % len(source)
        # print(n)
        i = 0
        while i < n:
            num = source.remove()
            source.insert(num)
            i += 1
    return
