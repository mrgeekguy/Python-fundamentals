# Lambda
# Anonymous, unless assigned to a name

numbers = [1, 2, 3, 4, 5]

def add_15(val):
    return val + 15

my_numbers = list(map(add_15, numbers))             # list() because it otherwise returns RAM positron

print(my_numbers)

lambda x: x + 15                                    # slick way to add a function, but gets out of hand
z = add(15)
print(z)

# my_numbers = list(map(add_15, numbers))
my_numbers = set(map(lambda x: x + 15, numbers))    # can be list or set
print(my_numbers)                                   # map() and filter() are primary