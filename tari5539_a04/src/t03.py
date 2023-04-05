"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-02-11"
-------------------------------------------------------
"""
# Imports
#from Queue_array import Queue
from Queue_circular import Queue
from functions import queue_combine
# Constants

source1 = Queue()
source2 = Queue()
target = Queue()

source1.insert(11)
source1.insert(22)
source1.insert(33)
# source1.insert(44)
# source1.insert(55)
print("source1:", source1._values)

source2.insert(111)
source2.insert(222)
source2.insert(333)
print("source2:", source2._values)

# target.insert(0)
#print("target:", target._values)

target = queue_combine(source1, source2)
print("new source1:", source1._values)
print("new source2:", source2._values)
print("target:", target._values)
