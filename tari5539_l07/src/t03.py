"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-03-08"
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
lst2.append(11)
lst2.append(22)
lst2.append(33)
lst2.append(44)
# print("lst2")
# for v in lst2:
# print(v)

even, odd = lst1.split_alt()
print("even")
for v in even:
    print(v)
print("odd")
for v in odd:
    print(v)
"""
lst1._move_front_to_rear(lst2)
print("new lst1")
for v in lst1:
    print(v)

print("new lst2")
for v in lst2:
    print(v)
"""
