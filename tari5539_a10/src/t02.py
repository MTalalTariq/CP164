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
from List_linked import List
from Sorts_List_linked import Sorts
# Constants

a1 = [55, 56, 54, 55, 21, 4, 72, 75, 71, 20]
a = List()
for v in a1:
    a.append(v)


Sorts.radix_sort(a)

for v in a:
    print(v)
