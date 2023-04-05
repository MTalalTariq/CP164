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
lst1.append(11)
print("lst1")
for v in lst1:
    print(v)

lst2 = List()
lst2.append(222)
lst2.append(333)
lst2.append(11)
lst2.append(555)
lst2.append(44)
print("lst2")
for v in lst1:
    print(v)


target = List()
target.intersection_r(lst1, lst2)


print("target")
for v in target:
    print(v)
