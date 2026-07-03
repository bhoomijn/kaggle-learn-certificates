# Lists - Q3
# Implement the Purple Shell effect: swap first and last racers

def purple_shell(racers):
    """Apply the Purple Shell effect in-place.
    
    Swaps the first place racer with the last place racer.
    
    Examples:
    >>> purple_shell(["Mario", "Luigi", "Peach", "Bowser"])
    ['Bowser', 'Luigi', 'Peach', 'Mario']
    >>> purple_shell(["Yoshi", "Toad"])
    ['Toad', 'Yoshi']
    >>> purple_shell(["Donkey Kong"])
    ['Donkey Kong']
    """
    if len(racers) < 2:
        return  # nothing to do
    
    # Swap first and last in-place
    racers[0], racers[-1] = racers[-1], racers[0]


# Example usage
race1 = ["Mario", "Luigi", "Peach", "Bowser"]
purple_shell(race1)
print(race1)  # Expected: ['Bowser', 'Luigi', 'Peach', 'Mario']

race2 = ["Yoshi", "Toad"]
purple_shell(race2)
print(race2)  # Expected: ['Toad', 'Yoshi']

race3 = ["Donkey Kong"]
purple_shell(race3)
print(race3)  # Expected: ['Donkey Kong']

# Kaggle grader check (keep only in Kaggle notebook)
q3.check()
