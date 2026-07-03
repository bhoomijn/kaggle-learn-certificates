# Booleans and Conditionals - Q5
# Does the customer want exactly one topping?

def exactly_one_topping(ketchup, mustard, onion):
    """Return True if the customer wants exactly one topping.
    
    Parameters:
    ketchup (bool): True if ketchup is chosen
    mustard (bool): True if mustard is chosen
    onion (bool): True if onion is chosen
    
    Examples:
    >>> exactly_one_topping(True, False, False)
    True
    >>> exactly_one_topping(False, True, False)
    True
    >>> exactly_one_topping(True, True, False)
    False
    >>> exactly_one_topping(False, False, False)
    False
    >>> exactly_one_topping(False, False, True)
    True
    """
    return int(ketchup) + int(mustard) + int(onion) == 1


# Example usage
print(exactly_one_topping(True, False, False))   # Expected True
print(exactly_one_topping(False, True, False))   # Expected True
print(exactly_one_topping(True, True, False))    # Expected False
print(exactly_one_topping(False, False, False))  # Expected False
print(exactly_one_topping(False, False, True))   # Expected True

# Kaggle grader check (keep only in Kaggle notebook)
q5.check()
