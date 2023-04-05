"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-03-26"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from Letter import fill_letter_bst
from functions import do_comparisons, comparison_total, letter_table
# Constants
DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"


bst1 = BST()
bst2 = BST()
bst3 = BST()
fill_letter_bst(bst1, DATA1)
fill_letter_bst(bst2, DATA2)
fill_letter_bst(bst3, DATA3)

fn = "gibbon.txt"
fv = open(fn, "r", encoding="utf-8")
do_comparisons(fv, bst1)
t1 = comparison_total(bst1)
fv = open(fn, "r", encoding="utf-8")
do_comparisons(fv, bst2)
t2 = comparison_total(bst2)
fv = open(fn, "r", encoding="utf-8")
do_comparisons(fv, bst3)
t3 = comparison_total(bst3)


print("Comparing by order: ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print("{}".format(t1))
print("------------------------------------------------------------")
print("Comparing by order: MFTCJPWADHKNRUYBEIGLOQSVXZ")
print("{}".format(t2))
print("------------------------------------------------------------")
print("Comparing by order: ETAOINSHRDLUCMPFYWGBVKJXZQ")
print("{}".format(t3))
print("------------------------------------------------------------")

letter_table(bst1)
