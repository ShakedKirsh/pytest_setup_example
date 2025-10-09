"""
A function called count_words that takes a string as
an argument and returns the number of words in that string.
"""

def count_words(string):
    count = len(string.split(" "))
    if len(string) < 1:
        raise Exception("String is empty!")
    return count