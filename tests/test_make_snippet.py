from lib.make_snippet import *
"""
If no string is entered, return empty string
"""

def test_make_snippet_empty_string():
    result = make_snippet("")
    assert result == ""

"""
If string given is under 4 words, return string.
"""
def test_make_snippet_under_5():
    assert make_snippet("One Two Three Four") == "One Two Three Four"

"""
If string longer than 5 words, cut off and add '...'
"""

def test_make_snippet_string_longer_than_five():
    result = make_snippet("One Two Three Four Five Six")
    assert result == "One Two Three Four Five ..."