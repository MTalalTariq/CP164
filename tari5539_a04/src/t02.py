"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-02-08"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
# Constants

target1 = Queue()
target2 = Queue()

target1.insert(2)
target1.insert(5)
print("target1:", target1._values)


target2.insert(2)
target2.insert(5)
target2.remove()
target2.insert(2)
target2.insert(5)
target2.remove()
print("target2:", target2._values)

print(target1 == target2)
