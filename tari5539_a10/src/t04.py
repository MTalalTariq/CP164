"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-04-04"
-------------------------------------------------------
"""
# Imports
from Sorts_Deque_linked import Sorts
from Deque_linked import Deque


a1 = [55, 56, 54, 55, 21, 4, 72, 75, 71, 20]
a = Deque()
for v in a1:
    a.insert_rear(v)


Sorts.gnome_sort(a)
for v in a:
    print(v)
