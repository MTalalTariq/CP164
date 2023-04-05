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
lst.append(22)
lst.append(33)
lst.append(22)

index = 0
for v in lst:
    print(f"{index}:", v)
    index += 1

key = 55
print(f"FIND: key: {key}, value: {lst.find(key)}")
key = 55
print(f"INDEX: key: {key}, index: {lst.index(key)}")
key = 1
print(f"__CONTAINS__: key: {key}, contains? {key in lst}")
