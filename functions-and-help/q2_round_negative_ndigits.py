# Functions and Getting Help - Q2
# Exploring round() behavior when ndigits is negative

# Put your test code here
print(round(1234.56, -1))   # Rounds to nearest 10 → 1230
print(round(1234.56, -2))   # Rounds to nearest 100 → 1200
print(round(1234.56, -3))   # Rounds to nearest 1000 → 1000
print(round(1234.56, 0))    # Rounds to nearest integer → 1235
print(round(1234.56, 2))    # Rounds to 2 decimal places → 1234.56
