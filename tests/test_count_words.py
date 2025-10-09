import pytest
from lib.count_words import count_words
"""
Takes string with 5 words returns 5.
"""

def test_count_words_string_5_words():
    result = count_words("one two three four five")
    assert result == 5

"""
When an empty string is given, return zero.
"""
def test_count_words_empty_string():
    with pytest.raises(Exception) as e: # <-- New code
        count_words("")
    error_message = str(e.value) # <-- New code
    assert error_message == "String is empty!"
