# Loops and List Comprehensions - Q4
# Slot machine simulation

from learntools.python import slot_machine

def play_n_times(n):
    """Play the slot machine n times and return total winnings.
    
    Parameters:
    n (int): Number of times to play
    
    Returns:
    int: Total winnings after n plays
    """
    total = 0
    for i in range(n):
        winnings = slot_machine.play_slot_machine()
        total += winnings
        # Logging each play
        print(f"Play {i+1}: Won ${winnings}, Total = ${total}")
    return total


# Example usage
print("Total winnings after 10 plays:", play_n_times(10))

# Kaggle grader check (keep only in Kaggle notebook)
q4.check()
