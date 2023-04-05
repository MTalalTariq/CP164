"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2023-02-04"
-------------------------------------------------------
"""
# Imports
from functions import is_mirror_stack
# Constants


string = "Abcm"
valid_chars = "abc"
m = 'm'

mirror = is_mirror_stack(string, valid_chars, m)
print(f"str: '{string}', valid_chars: {valid_chars}', m: '{m}'")
print(mirror, mirror.value)
