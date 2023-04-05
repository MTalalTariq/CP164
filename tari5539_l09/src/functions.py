"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-03-23"
-------------------------------------------------------
"""
# Imports

# Constants

# task1


def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
    Hash     Slot Key
    -------- ---- --------------------
    1652346    3 Dark City, 1998
    848448    6 Zulu, 1964
    Do not create an actual Hash_Set.
    Use: hash_table(slots, values)
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """
    print("Hashes")
    print("Hash     Slot Key")
    print("======== ==== ====================")
    for i in values:
        h = hash(i)
        slot = h % 7
        f_str = i.key()
        print(f"{h:8}{slot:5} {f_str}")
    return
