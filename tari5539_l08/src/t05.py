"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-03-14"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from morse import fill_letter_bst
from morse import encode_morse
from morse import DATA1
# Constants
text = "FORTNITE RED"
print("English:")
print(text)
bst = BST()
fill_letter_bst(bst, DATA1)
# print(bst._count)
print("Morse Code:")
code = encode_morse(bst, text)
print(code)
