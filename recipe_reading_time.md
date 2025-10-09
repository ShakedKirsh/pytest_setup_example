# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute._

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def estimate_reading_time(text):
    """Calculates reading time for a text

    Parameters: (list all parameters and their types)
        text: a string of human-readable text

    Returns: (state the return value and its type)
        a float: representing an estimated reading time in minutes e.g. 4.5

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a text of 200 words
It returns 1.0
"""
estimate_reading_time("...200....") => 1.0

"""
Given a text of 50 words
It returns 0.25
"""
estimate_reading_time("...50...") => 0.25

"""
Given a text of 400
It returns 2.0
"""
estimate_reading_time("...400...") => 2.0

"""
Given an empty string
It returns 0
"""
estimate_reading_time("") => 0

"""
Given a text without words (such as number or characters)
It returns an error message
"""
estimate_reading_time("234 !£$") => "Text does not contain words"

"""
Given a text with 500 words and characters/numbers 
It returns the the right number without problem
"""
estimate_reading_time("...500...") => 2.5

"""
Given a None value
It throws an error
"""
estimate_reading_time(None) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.estimate_reading_time import *

"""
Given a text of 200 words
It returns 1.0
"""
def estimate_reading_time_200_words():
    result = estimate_reading_time("...200...")
    assert result == 1.0
```

Ensure all test function names are unique, otherwise pytest will ignore them!
