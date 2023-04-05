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
from Sorted_List_array import Sorted_List
from Movie import Movie
# Constants

# insert and remove and remove front
"""
source = Sorted_List()
source.insert(4)
source.insert(3)
source.insert(2)
source.insert(4)
source.insert(5)
print("source:", source._values)
print("peek:", source.peek())
print("removed:", source.remove(4))
print("source:", source._values)
print("removed front:", source.remove_front())
print("source:", source._values)
"""

# find
"""
source = Sorted_List()
m1 = Movie("title1", 1888, "direc", 2.9, [0, 2, 3, 4, 5])
source.insert(m1)
key = Movie("title1", 1888, None, None, None)
print(f"find {key}")
print("found:", source.find(key))
"""

# max and min and index
"""
source = Sorted_List()
source.insert(4)
source.insert(3)
source.insert(2)
source.insert(4)
source.insert(5)
print("source:", source._values)
print("max:", source.max(), "min:", source.min())
key = 5
print(f"index of key {key}:", source.index(key))
"""

# count
"""
source = Sorted_List()
source.insert(4)
source.insert(4)
source.insert(4)
source.insert(10)
source.insert(2)
print("source:", source._values)
key = 2
print(f"count with key {key}:", source.count(key))
"""

# remove_many
"""
source = Sorted_List()
source.insert(4)
source.insert(1)
source.insert(2)
source.insert(2)
source.insert(10)
print("source:", source._values)
key = 4
print(f"remove many with key {key}")
source.remove_many(key)
print("new source:", source._values)
"""

# __contains___ and __getitem__
"""
source = Sorted_List()
source.insert(4)
source.insert(1)
source.insert(2)
print("source:", source._values)
key = 3
print(f"contains {key}?", key in source)
i = 0
print(f"get ietm index {i}:", source[i])
"""

# __eq__
"""
source = Sorted_List()
target = Sorted_List()
source.insert(4)
source.insert(1)
source.insert(2)
target.insert(4)
target.insert(1)
target.insert(100)
print("source:", source._values)
print("target:", target._values)
print("equal?", source == target)
"""

# clean
"""
source = Sorted_List()
source.insert(4)
source.insert(1)
source.insert(4)
source.insert(4)
source.insert(1)
source.insert(2)
print("source:", source._values)
source.clean()
print("new source:", source._values)
"""

# intersection
"""
target = Sorted_List()
target.insert(1)
print("target:", target._values)

source1 = Sorted_List()
source1.insert(1)
source1.insert(1)
source1.insert(2)
source1.insert(3)
source1.insert(6)
print("source1:", source1._values)

source2 = Sorted_List()
source2.insert(1)
source2.insert(2)
source2.insert(4)
source2.insert(6)
source2.insert(6)
print("source2:", source2._values)
target.intersection(source1, source2)
print("new target:", target._values)
"""

# split
"""
source = Sorted_List()
source._values = [1, 2, 3, 4]
source.insert(5)
print("source:", source._values)
target1, target2 = source.split()
print("new source:", source._values)
print("target1:", target1._values)
print("target2:", target2._values)
"""

# split_alt
"""
source = Sorted_List()
source._values = [1, 2, 3, 4, 5, 6, 7]
print("source:", source._values)
target1, target2 = source.split_alt()
print("new source:", source._values)
print("target1:", target1._values)
print("target2:", target2._values)
"""

# split_key
"""
source = Sorted_List()
source._values = [1, 2, 3, 4, 5, 6, 7]
print("source:", source._values)
key = 4
print("key:", key)
target1, target2 = source.split_key(key)
print("new source:", source._values)
print("target1:", target1._values)
print("target2:", target2._values)
"""

# union
# """
source1 = Sorted_List()
source2 = Sorted_List()
target = Sorted_List()
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
# """
