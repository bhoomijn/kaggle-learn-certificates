# Functions and Getting Help - Q1
# Complete the body of the following function according to its docstring

def round_to_two_places(num):
    """Return the given number rounded to two decimal places.
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    return round(num, 2)

# Quick test
print(round_to_two_places(3.14159))   # Output: 3.14
print(round_to_two_places(9.8765))    # Output: 9.88
