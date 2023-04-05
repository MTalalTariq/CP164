"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-03-01"
-------------------------------------------------------
"""
# Imports
from List_linked import List
# Constants

lst = List()

lst.append(44)
lst.append(55)
lst.append(11)
lst.append(33)
lst.append(22)

index = 0
for v in lst:
    print(f"{index}:", v)
    index += 1
key = 55
previous, current, index = lst._linear_search(key)
try:
    print(
        f"key: {key}, prev: {previous._value}, curr: {current._value}, index: {index}")
except:
    print(
        f"key: {key}, prev: {previous}, curr: {current}, index: {index}")
