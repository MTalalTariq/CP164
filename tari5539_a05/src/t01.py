"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-02-18"
-------------------------------------------------------
"""
# Imports
from List_array import List
# Constants

# __eq__
"""
source = List()
target = List()
source._values = [1, 2, 3]
target._values = [1, 2, 3]
print("source:", source._values)
print("target:", target._values)
print(source == target)
source._values = [1, 2, 90]
target._values = [10, 2, 3]
print("source:", source._values)
print("target:", target._values)
print(source == target)
"""

# clean
"""
source = List()
source._values = [100, 1, 2, 2, 2, 3, 3, 1, 100, 2]
print("source:", source._values)
source.clean()
print("new source:", source._values)

source._values = [1, 2, 4, 5]
print("source:", source._values)
source.clean()
print("new source:", source._values)
"""

# combine
"""
source1 = List()
source2 = List()
target = List()
source1._values = [1, 2, 3]
source2._values = [6, 7, 8]
print("source1:", source1._values)
print("source2:", source2._values)
target.combine(source1, source2)
print("new source1:", source1._values)
print("new source2:", source2._values)
print("target:", target._values)
"""

# intersection
"""
source1 = List()
source2 = List()
target = List()
source1._values = [1, 2, 3, 8, 9, 9]
source2._values = [6, 7, 8, 8, 9, 9]
target._values = [1, 2, 8]
print("source1:", source1._values)
print("source2:", source2._values)
print("target:", target._values)
target.intersection(source1, source2)
print("new source1:", source1._values)
print("new source2:", source2._values)
print("new target:", target._values)
"""

# prepend
"""
source = List()
source._values = [1, 2, 3]
value = 4
print("value:", value)
print("source:", source._values)
source.prepend(value)
print("new source:", source._values)
"""

# remove_front
"""
source = List()
source._values = [1, 2, 2, 4]
print("source:", source._values)
print("removed from front:", source.remove_front())
print("new source:", source._values)
"""

# remove_many
"""
source = List()
source._values = [1,2,2,3]
print("source:", source._values)
key = 2
print("key:", key)
source.remove_many(key)
print("new source:", source._values)
"""

# split
"""
source = List()
source._values = [1, 2, 3, 4, 5]
print("source:", source._values)
target1, target2 = source.split()
print("new source:", source._values)
print("target1:", target1._values)
print("target2:", target2._values)
"""

# split_alt
# """
source = List()
source._values = [1, 2, 3, 4, 5]
print("source:", source._values)
target1, target2 = source.split_alt()
print("new source:", source._values)
print("target1:", target1._values)
print("target2:", target2._values)
# """

# union
"""
source1 = List()
source2 = List()
target = List()
source1._values = [1, 2, 3, 8, 9, 9, 11]
source2._values = [6, 7, 8, 8, 9, 9, 10, 10]
target._values = [1, 2, 8]
print("source1:", source1._values)
print("source2:", source2._values)
print("target:", target._values)
target.union(source1, source2)
print("new source1:", source1._values)
print("new source2:", source2._values)
print("new target:", target._values)
"""
