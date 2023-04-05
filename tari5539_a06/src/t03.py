"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-03-07"
-------------------------------------------------------
"""
# Imports
from Deque_linked import Deque
# Constants

#insert and remove
"""
dq = Deque()
dq.insert_front(3)
dq.insert_front(1)
dq.insert_front(2)
dq.insert_front(3)
dq.insert_rear(6)
dq.insert_rear(7)
print("dq")
dq.print()
dq.remove_front()
dq.remove_front()
dq.remove_rear()
print("new dq")
dq.print()
"""

# swap
# """
dq = Deque()
dq.insert_rear(1)
dq.insert_rear(2)
dq.insert_rear(3)
dq.insert_rear(4)
dq.insert_rear(5)
dq.insert_rear(6)
dq.insert_rear(7)
dq.insert_rear(8)
dq.insert_rear(9)
dq.insert_rear(10)
print("dq")
dq.print()
#l = dq._front._next
#l = dq._front
l = dq._front._next

#r = dq._front._next._next._next
#r = dq._rear
r = dq._front._next._next
dq._swap(l, r)
print("new dq")
dq.print()
# """
