# Loops and List Comprehensions - Q3
# Return True if any meal is repeated two days in a row

def menu_is_boring(meals):
    """Given a list of meals served over some period of time, 
    return True if the same meal has ever been served two days in a row, 
    and False otherwise.
    
    Examples:
    >>> menu_is_boring(["dal", "roti", "dal", "dal"])
    True
    >>> menu_is_boring(["pizza", "burger", "pasta"])
    False
    >>> menu_is_boring([])
    False
    >>> menu_is_boring(["idli"])
    False
    """
    for i in range(len(meals) - 1):
        if meals[i] == meals[i + 1]:
            return True
    return False


# Example usage
print(menu_is_boring(["dal", "roti", "dal", "dal"]))   # Expected True
print(menu_is_boring(["pizza", "burger", "pasta"]))    # Expected False
print(menu_is_boring([]))                              # Expected False
print(menu_is_boring(["idli"]))                        # Expected False

# Kaggle grader check (keep only in Kaggle notebook)
q3.check()
