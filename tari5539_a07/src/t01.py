"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-03-11"
-------------------------------------------------------
"""
# Imports
from List_linked import List
# Constants

# clean
"""
lst = List()
lst.append(99)
lst.append(99)
lst.append(99)
lst.append(99)
lst.append(99)
print("lst")
for v in lst:
    print(v)

lst.clean()

print("new lst")
for v in lst:
    print(v)


"""
# combine
"""
source1 = List()
source1.append(99)
source1.append(99)
source1.append(99)
source1.append(99)
print("source1")
for v in source1:
    print(v)
source2 = List()
source2.append(88)
source2.append(88)
print("source2")
for v in source2:
    print(v)
target = List()
target.append(1)
print("target")
for v in target:
    print(v)
target.combine(source1, source2)
print("new source1")
for v in source1:
    print(v)
print("new source2")
for v in source2:
    print(v)
print("new target")
for v in target:
    print(v)

"""

# split
# """
lst = List()
lst.append(11)
lst.append(22)
lst.append(33)
lst.append(44)
lst.append(55)
print("lst")
for v in lst:
    print(v)
target1, target2 = lst.split()
print("target1")
for v in target1:
    print(v)
print("target2")
for v in target2:
    print(v)
# """
