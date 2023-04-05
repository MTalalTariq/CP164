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
from morse import fill_code_bst
from morse import decode_morse
from morse import DATA2
# Constants

code = "... --- ..."
#code = ""
print("Morse Code:")
print(code)

bst = BST()
fill_code_bst(bst, DATA2)

print("English:")
text = decode_morse(bst, code)
print(text)
