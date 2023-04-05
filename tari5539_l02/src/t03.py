"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-01-22"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from utilities import stack_to_array
# Constants

s = Stack()
num = [11, 22, 33, 44, 55]

for i in range(0, len(num)):
    s.push(num[i])

# s._values = num  # filling up stack values with num

target = []

print("stack values:", s._values)
print("target:", target)
stack_to_array(s, target)
print("new stack values:", s._values)
print("new target:", target)
