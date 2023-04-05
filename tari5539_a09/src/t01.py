"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-04-01"
-------------------------------------------------------
"""
# Imports
from Hash_Set_array import Hash_Set
from functions import insert_words, comparison_total
# Constants

filename = "gibbon.txt"
fv = open(filename, "r", encoding="utf-8")
# encoding="utf-8"

hs = Hash_Set(20)

insert_words(fv, hs)
fv.close()
total, max_word = comparison_total(hs)

print("Using array-based list Hash_Set")
print()
print(f"Total Comparisons: {total:,}")
print(
    f"Word with maximum comparisons '{max_word.word}': {max_word.comparisons:,}")
