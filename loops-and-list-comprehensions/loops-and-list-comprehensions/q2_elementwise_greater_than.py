# Loops and List Comprehensions - Q2
# Element-wise comparison of list elements against n

def elementwise_greater_than(L, n):
    """Return a list of booleans indicating whether each element of L is greater than n.
    
    Parameters:
    L (list): List of numbers
    n (int or float): Number to compare against
    
    Examples:
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    >>> elementwise_greater_than([10, 5, 0], 5)
    [True, False, False]
    """
    return [x > n for x in L]


# Example usage
print(elementwise_greater_than([1, 2, 3, 4], 2))   # Expected: [False, False, True, True]
print(elementwise_greater_than([10, 5, 0], 5))     # Expected: [True, False, False]

# Kaggle grader check (keep only in Kaggle notebook)
q2.check()
