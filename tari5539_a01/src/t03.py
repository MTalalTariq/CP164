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
from functions import find_subs
# Constants

string = "It was a really, really, big assignment."
sub = "real"
locations = find_subs(string, sub)
print(locations)
