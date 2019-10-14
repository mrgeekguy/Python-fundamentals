# Variables

any_name = "Yes"

# Strings - type of class in Python; immutable; fully encapsulates
# can manipulate with a .method()
# in classes, functions are .method()

# Numbers (3 types)
# Integers int()
# Floats float()
# Complex (ie: 2 + 2j)

# Collections
    # List
    # Tuple - can declare multiple variables in one line and unpack it
    # Set
    # Dictionary

def multiple_returns(a, b):
    data = 0
    if a > b:
        data = b, a
    return True, data

print(multiple_returns(2, 1))

success, coordinate = multiple_returns(2, 1)

# 