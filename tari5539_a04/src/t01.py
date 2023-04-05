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
from Queue_circular import Queue
# Constants
"""
target = Queue()
print(target._values)
target.insert(1)
print(target._values)
target.insert(2)
print(target._values)
target.remove()
print(target._values)
"""
target1 = Queue(3)
target2 = Queue(4)

target1.insert(2)
target1.insert(5)
print("target1:", target1._values)


target2.insert(1)
target2.insert(3)
target2.insert(3)
target2.insert(2)
target2.remove()
target2.remove()
target2.remove()
target2.insert(5)

print("target2:", target2._values)
#print("rears", target1._rear, target2._rear)
#print("front", target1._front, target2._front)
print(target1 == target2)
