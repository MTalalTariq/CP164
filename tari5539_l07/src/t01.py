"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-03-09"
-------------------------------------------------------
"""
# Imports
from List_linked import List
# Constants

lst1 = List()
lst1.append(22)
lst1.append(33)
lst1.append(11)
lst1.append(55)
lst1.append(44)
print("lst1")
for v in lst1:
    print(v)

p, c, i = lst1._linear_search(333)

print("p:", p)
print("c:", c)
print("i:", i)
