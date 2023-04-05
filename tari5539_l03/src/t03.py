"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-01-24"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
from utilities import array_to_queue
from utilities import queue_to_array
from utilities import queue_test
# Constants

print("testing array_to_queue")
source = [1, 2, 3, 4, 5]
q = Queue()
print("queue values", q._values)
print("source", source)
array_to_queue(q, source)
print("new queue values", q._values)
print("new source", source)

print("_________________")
print("testing queue_to_array")
target = []
q = Queue()
q._values = [1, 2, 3, 4, 5]
print("queue values", q._values)
print("target", target)
queue_to_array(q, target)
print("new queue values", q._values)
print("new target", target)

print("_________________")
print("testing queue_test")
a = [1, 2, 3, 4, 5]
queue_test(a)
