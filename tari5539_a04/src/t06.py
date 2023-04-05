"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-02-12"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue
# Constants

source = Priority_Queue()
source.insert(11)
source.insert(2)
source.insert(30)
source.insert(1)
source.insert(10)
source.insert(9)
source.insert(4)

key = 4
print("key:", key)
print("source:", source._values)
target1, target2 = source.split_key(key)
print("target1:", target1._values)
print("target1:", target2._values)
print("new source:", source._values)
