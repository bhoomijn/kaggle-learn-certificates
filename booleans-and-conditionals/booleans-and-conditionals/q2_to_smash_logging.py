# Booleans and Conditionals - Q2
# Add logging to the to_smash function

def to_smash(total_candies, n_friends=3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between friends.

    Parameters:
    total_candies (int): Total number of candies collected.
    n_friends (int, optional): Number of friends to split candies between.
                               Defaults to 3.

    Examples:
    >>> to_smash(91)
    1
    >>> to_smash(91, 7)
    0
    >>> to_smash(10, 2)
    0
    """
    smashed = total_candies % n_friends
    # Logging (debugging info)
    print(f"[LOG] Total candies: {total_candies}, Friends: {n_friends}, To smash: {smashed}")
    return smashed


# Example usage
print("Default (3 friends):", to_smash(91))       # Expected output: 1
print("Custom (7 friends):", to_smash(91, 7))    # Expected output: 0
print("Two friends:", to_smash(10, 2))           # Expected output: 0

# Kaggle grader check (keep only in Kaggle notebook)
q2.check()
