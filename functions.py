# Function
# 

# def function_name_here(parameters): # way to create default value in parameter
#     # code block
#     return # some data

function_name_here("parameter data")

def function_name_here(x):
    print(x)
    return "some data"

function_name_here("parameter data")
print(function_name_here("Python is cool"))

# Multiple parameters

def cash_register(total, tendered):
    """ This takes two numbers and compares them """ # doc_string
    answer = ""
    if tendered < total:
        answer = "I need more money"
    elif tendered == total:
        answer = "Have a nice day"
    else:
        answer = "I owe you some money"
    return answer

# scope - variable visibility
# Sequential Inerpreted Language
# top to bottom interpreting

answer = cash_register(67, 30)

# Default return statement - None

def combine(x, y, z):
    """ Takes 3 numbers and prints sum """
    return (x + y + z)

what_is_this = combine(1,2,3)

print(what_is_this)

