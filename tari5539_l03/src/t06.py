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
from Priority_Queue_array import Priority_Queue
from utilities import array_to_pq
from utilities import pq_to_array
from utilities import priority_queue_test
from Movie import Movie
# Constants

print("testing array_to_pq")
source = [1, 2, 3, 4, 5]
pq = Priority_Queue()
print("pq values", pq._values)
print("source", source)
array_to_pq(pq, source)
print("new pq values", pq._values)
print("new source", source)

print("_________________")
print("testing pq_to_array")
target = []
pq = Priority_Queue()
pq.insert(4)
pq.insert(20)
pq.insert(6)
pq.insert(9)
pq.insert(5)
print("pq values", pq._values)
print("target", target)
pq_to_array(pq, target)
print("new pq values", pq._values)
print("new target", target)

print("_________________")
print("testing priority_queue_test")
a = [11, 4, 6, 7, 3, 12]
priority_queue_test(a)
