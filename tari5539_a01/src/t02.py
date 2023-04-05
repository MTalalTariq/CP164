"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-01-15"
-------------------------------------------------------
"""
# Imports
from functions import file_analyze
# Constants

fv = open("task2text.txt", "r", encoding="utf-8")
u, l, d, w, r = file_analyze(fv)
print(u, l, d, w, r)
fv.close()
