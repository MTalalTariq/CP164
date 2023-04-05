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
from Word import Word
#from Hash_Set_array import Hash_Set
# Constants

# task1


def insert_words(fv, hash_set):
    """
    -------------------------------------------------------
    Retrieves every Word in file_variable and inserts into
    a Hash_Set. Each Word object in hash_set contains the number
    of comparisons required to insert that Word object from
    file_variable into hash_set.
    Use: insert_words(file_variable, hash_set)
    -------------------------------------------------------
    Parameters:
        fv - the already open file containing data to evaluate (file)
        hash_set - the Hash_Set to insert the words into (Hash_Set)
    Returns:
        None
    -------------------------------------------------------
    """
    # fv.seek(0)

    fv = fv.readlines()
    for line in fv:
        word_list = line.split(" ")
        # words
        for word in word_list:
            if word.isalpha() is True:
                word = Word(word.lower())
                hash_set.insert(word)
    # fv.close()
    return


def comparison_total(hash_set):
    """
    -------------------------------------------------------
    Sums the comparison values of all Word objects in hash_set.
    Use: total, max_word = comparison_total(hash_set)
    -------------------------------------------------------
    Parameters:
        hash_set - a hash set of Word objects (Hash_Set)
    Returns:
        total - the total of all comparison fields in the Hash_Set
            Word objects (int)
        max_word - the word having the most comparisons (Word)
    -------------------------------------------------------
    """
    #max_word_count = 0
    max_word = Word("boo")
    total = 0
    """
    for slot in hash_set._table:
        for item in slot:
            total += item.comparisons
            if item.comparisons > max_word.comparisons:
                max_word = item
    """
    for word in hash_set:
        total += word.comparisons
        if word.comparisons > max_word.comparisons:
            max_word = word
    return total, max_word
