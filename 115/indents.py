def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    counter = 0
    for char in text:
        if char == ' ':
            counter += 1
        else:
            break
    return counter
