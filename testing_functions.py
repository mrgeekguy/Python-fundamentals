# Testing
# pip install pytest to install
# define tests with test_name_of_function()
# 

def find_largest(x, y):
    # or return max(x, y)
    if x > y:
        return x
    else:
        return y
    
def test_find_largest(): # put test before your function
    assert find_largest(1, 2) == 2 # assert what you think is correct

def test_something():
    assert "test" == "test"

# more examples in error_handling.py