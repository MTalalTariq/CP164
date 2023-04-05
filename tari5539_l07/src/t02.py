"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-03-07"
-------------------------------------------------------
"""
# Imports
from List_linked import List
# Constants

lst1 = List()
lst1.append(1)
lst1.append(2)
lst1.append(3)
lst1.append(4)
print("lst1")
for v in lst1:
    print(v)

lst2 = List()
lst2.append(1)
lst2.append(2)
lst2.append(3)
lst2.append(4)
print("lst2")
for v in lst2:
    print(v)

print("Identical?", lst1.is_identical(lst2))
print("Identical(r)?", lst1.is_identical_r(lst2))
