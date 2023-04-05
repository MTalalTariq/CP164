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
from Movie import Movie
# Constants

s = Stack()
b = s.is_empty()
print(f"The stack is empty: {b}")  # should be true

m1 = Movie('T1', 2000, 'D1', 5, [0, 1, 3, 9])
m2 = Movie('T2', 2001, 'D2', 5.5, [0, 4, 7])
#m3 = Movie('T3', 2006, 'D3', 5.6, [4, 8])

s.push(m1)
s.push(m2)
print("two movies added to stack")

b = s.is_empty()
print(f"The stack is empty: {b}")  # should be false

value = s.pop()
print(f"last movie in stack, {value.title}, has been removed")  # should be T2

value = s.peek()
print(f"last movie in stack is: {value.title}")  # should be T1
