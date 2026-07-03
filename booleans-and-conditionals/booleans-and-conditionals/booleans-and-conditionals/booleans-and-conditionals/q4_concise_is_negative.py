# Booleans and Conditionals - Q4
# Rewrite is_negative in a concise one-line form

def is_negative(num):
    """Return True if num is negative, False otherwise."""
    if num < 0:
        return True
    else:
        return False


def concise_is_negative(num):
    """Return True if num is negative, False otherwise (concise version)."""
    return num < 0


# Example usage
print(is_negative(-5))          # Expected True
print(is_negative(3))           # Expected False
print(concise_is_negative(-5))  # Expected True
print(concise_is_negative(3))   # Expected False

# Kaggle grader check (keep only in Kaggle notebook)
q4.check()
