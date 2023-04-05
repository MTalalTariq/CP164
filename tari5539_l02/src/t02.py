"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-01-21"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from utilities import array_to_stack
# Constants

s = Stack()

source = [11, 22, 33, 44]

print("stack values:", s._values)
print("source:", source)
array_to_stack(s, source)
print("new stack values:", s._values)
print("new source:", source)
