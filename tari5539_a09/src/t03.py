"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-04-02"
-------------------------------------------------------
"""
# Imports
from Hash_Set_BST import Hash_Set
from functions import insert_words, comparison_total
fn = "gibbon.txt"
fv = open(fn, "r", encoding="utf-8")
hs = Hash_Set(20)
insert_words(fv, hs)
total, max_word = comparison_total(hs)
print("Using linked BST Hash_Set")
print()
print("Total Comparisons: {:,}".format(total))
print("Word with maximum comparisons '{}': {:,}".format(
    max_word.word, max_word.comparisons))
