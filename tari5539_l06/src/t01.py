"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-02-28"
-------------------------------------------------------
"""
# Imports
from List_linked import List
# Constants

lst = List()
lst.prepend(99)
lst.prepend(2)
lst.prepend(5)
lst.append(3)
lst.append(1)
lst.insert(0, 1000)

index = 0
for v in lst:
    print(f"{index}:", v)
    index += 1
