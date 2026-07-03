# Booleans and Conditionals - Q1
# Define a function called 'sign' which returns -1, 0, or 1 based on input

def sign(num):
    """Return the sign of a number.
    
    Returns:
    -1 if num is negative
     0 if num is zero
     1 if num is positive
    
    Examples:
    >>> sign(-5)
    -1
    >>> sign(0)
    0
    >>> sign(7)
    1
    """
    if num < 0:
        return -1
    elif num > 0:
        return 1
    else:
        return 0


# Example usage
print(sign(-10))   # Expected output: -1
print(sign(0))     # Expected output: 0
print(sign(25))    # Expected output: 1

# Kaggle grader check (keep only in Kaggle notebook)
q1.check()
