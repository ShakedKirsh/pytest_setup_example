import pytest
from lib.estimate_reading_time import *
"""
Given a tet of 200 words
The function returns 1.0
"""
def test_estimate_reading_time_200_words():
    text = " ".join(["word" for i in range(0, 200)])
    result = estimate_reading_time(text)
    assert result == 1.0

"""
Given a text of 50 words
It returns 0.25
"""
def test_estimate_reading_time_50_words():
    text = " ".join(["word" for i in range(0, 50)])
    result = estimate_reading_time(text)
    assert result == 0.25

"""
Given a text of 400
It returns 2.0
"""
def test_estimate_reading_400_words():
    text = " ".join(["word" for i in range(0, 400)])
    result = estimate_reading_time(text)
    assert result == 2.0

"""
Given an empty string
It returns 0
"""
def test_estimate_reading_time_empty_string():
    with pytest.raises(Exception) as e:
        estimate_reading_time("")
    assert str(e.value) == "Invalid input!"

"""
Given a None value
It throws an error
"""
def test_estimate_reading_time_none_value():
    with pytest.raises(Exception) as e:
        estimate_reading_time(None)
    assert str(e.value) == "Invalid input!"