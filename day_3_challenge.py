# # Fill out the truth table
# a       b       not ((a and b) or b)
# ----------------------------------
# False   False     True
# True    False     True
# False   True
# True    True
# ========================================
# Each student that has an A in their name, print their age.
# Make your program able to handle any list of students (this format below)

students = [("AJ", 25), ("XD", 19), ("JA", 27), ("IS", 27)]

# How we've done it in school

for name, age in students: # tuple unpacking
    if "a" in name.lower():
        print(name, "is", age)

# Refactored solution
# for name, age in students:
#   print(name, "is", age) if "a" in name.lower()