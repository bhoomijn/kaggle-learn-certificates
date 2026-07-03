# Loops and List Comprehensions - Q1
# Fix the bug in has_lucky_number

def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky.
    A lucky list contains at least one number divisible by 7.
    
    Examples:
    >>> has_lucky_number([1, 2, 3, 14])
    True
    >>> has_lucky_number([1, 2, 3, 5])
    False
    >>> has_lucky_number([7])
    True
    >>> has_lucky_number([])
    False
    """
    for num in nums:
        if num % 7 == 0:
            return True
    return False


# Example usage
print(has_lucky_number([1, 2, 3, 14]))   # Expected True (14 divisible by 7)
print(has_lucky_number([1, 2, 3, 5]))    # Expected False
print(has_lucky_number([7]))             # Expected True
print(has_lucky_number([]))              # Expected False

# Kaggle grader check (keep only in Kaggle notebook)
q1.check()
