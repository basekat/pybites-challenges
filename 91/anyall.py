VOWELS = 'aeiou'
PYTHON = 'python'


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    return set(input_str.lower()).issubset(set(VOWELS))

def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    return bool(set(PYTHON) & set(input_str.lower()))

def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    digits = '1234567890'
    return bool(set(input_str) & set(digits))
