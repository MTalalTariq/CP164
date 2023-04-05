"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-01-30"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from functions import stack_split_alt
# Constants

source = Stack()
#num = [1, 2, 3, 4, 5, 6, 7]
num = [8, 14, 12, 9, 8, 7, 5]
for i in num:
    source.push(i)
print("Source stack:", num)
target1, target2 = stack_split_alt(source)
print("target1:", target1._values)
print("target2:", target2._values)
