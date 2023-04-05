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
# Constants

pq = Priority_Queue()

pq.insert(22)
pq.insert(33)
pq.insert(11)
pq.insert(55)
pq.insert(44)

print(f"{pq.remove()} has been removed")
print(f"{pq.peek()} is the highest priority at index {pq._first}")
