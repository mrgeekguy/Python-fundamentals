# Error Handling
# Try Except

import pytest           # Dependency for Test Driven Development (TDD)
                        # Used in testing_functions.py

def proclaim_user_birthday(name, age):
    try:
        new_age = age + 1
        message = f"{ name } is now { new_age } years old!"
        print(message)
    except Exception as e:                          # put exception in variable e
        print(e)

proclaim_user_birthday("Adam", "45")

def find_user(user_id):
    """ Handling user_id lookup """
    if not isinstance(user_id, int):                # if user_id is not an integer
        try:
            user_id = int(user_id)                  # try modyfing user_id into int
        except Exception as e:
            raise TypeError("user_id must be a number")
    return "A user"
        # handle looking up the user here

def test_find_user_returns_string():
    assert find_user(2) == "A user"                 # only assert True

def test_find_user_takes_string_returns_string():
    assert find_user("2") == "A user"

def test_find_user_typerror_exception():
    with pytest.raises(TypeError):                  # with 
        find_user("string")

# find_user(12)
# find_user("44")
# try:
#     find_user(11)
# except 