# Lists - Q5
# Determine if a guest is fashionably late

def fashionably_late(arrivals, name):
    """Return True if the guest is fashionably late.
    
    A guest is fashionably late if they arrived 
    after at least half of the guests, but not last.
    
    Parameters:
    arrivals (list): List of guest names in order of arrival.
    name (str): Guest name to check.
    
    Examples:
    >>> party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
    >>> fashionably_late(party_attendees, 'Mona')
    True
    >>> fashionably_late(party_attendees, 'Gilbert')
    True
    >>> fashionably_late(party_attendees, 'Ford')
    False
    >>> fashionably_late(party_attendees, 'Adela')
    False
    """
    index = arrivals.index(name)
    return index >= len(arrivals) / 2 and index != len(arrivals) - 1


# Example usage
party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']

print(fashionably_late(party_attendees, 'Mona'))     # Expected True
print(fashionably_late(party_attendees, 'Gilbert'))  # Expected True
print(fashionably_late(party_attendees, 'Ford'))     # Expected False
print(fashionably_late(party_attendees, 'Adela'))    # Expected False

# Kaggle grader check (keep only in Kaggle notebook)
q5.check()
