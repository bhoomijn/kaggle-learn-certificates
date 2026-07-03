# Booleans and Conditionals - Q3
# Prove that prepared_for_weather function is buggy

def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    # Original buggy code
    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

# Test case where function gives wrong result
# According to logic: If it's not raining and it's not a workday, I'm safe → should return True
# But buggy code returns False

have_umbrella = False
rain_level = 0.0
have_hood = False
is_workday = False

actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print("Buggy function result:", actual)  # Expected True, but returns False

# Kaggle grader check (keep only in Kaggle notebook)
q3.check()
