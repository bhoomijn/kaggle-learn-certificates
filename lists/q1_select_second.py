# Lists - Q1
# Return the second element of a list, or None if it doesn't exist

def select_second(L):
    """Return the second element of the given list. 
    If the list has no second element, return None.
    
    Examples:
    >>> select_second([1, 2, 3])
    2
    >>> select_second([5])
    None
    >>> select_second([])
    None
    """
    if len(L) >= 2:
        return L[1]
    else:
        return None


# Example usage
print(select_second([1, 2, 3]))   # Expected output: 2
print(select_second([5]))         # Expected output: None
print(select_second([]))          # Expected output: None

# Kaggle grader check (keep only in Kaggle notebook)
q1.check()
