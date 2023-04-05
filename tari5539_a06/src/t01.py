"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-03-06"
-------------------------------------------------------
"""
# Imports
from Queue_linked import Queue
# Constants
# movefronttorear
"""
print("move front to rear")
target = Queue()
target.insert(1)
target.insert(2)
target.insert(3)
target.insert(4)
print("target")
target.print()

source = Queue()
source.insert(10)
source.insert(11)
source.insert(12)
print("source")
source.print()

target._move_front_to_rear(source)
print("new target")
target.print()
print("new source")
source.print()
"""

# combine
"""
target = Queue()
target.insert(1)
target.insert(2)
target.insert(3)
target.insert(4)
print("target")
target.print()

source1 = Queue()
source1.insert(10)
source1.insert(11)
source1.insert(12)
print("source1")
source1.print()

source2 = Queue()
source2.insert(20)
source2.insert(21)
source2.insert(22)
print("source2")
source2.print()

target.combine(source1, source2)
print("new target")
target.print()
print("new source1")
source1.print()
print("new source2")
source2.print()
"""

# split alt
# """
source = Queue()
source.insert(1)
source.insert(2)
source.insert(3)
source.insert(4)
source.insert(5)
print("source")
source.print()

target1, target2 = source.split_alt()
print("new source")
source.print()
print("target1")
target1.print()
print("target2")
target2.print()
# """
