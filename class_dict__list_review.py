# list with 3 dict and 2 kvp
to_filter = [
    {"name": "Jeff",
    "age": 25
    },
    {"name": "John",
    "age": 67
    },
    {"name": "Tim",
    "age": 57
    }
]
# filtereted_list = []
# for i in to_filter:
#     if to_filter["age"] > 50:
#         filtereted_list.append(i)

# OR

def filter_by_age(value):
    return value["age"] > 50

greater_than_50 = list(filter(filter_by_age, to_filter))



def im_gonna_be_a_callback(x):
    print(x)

def i_take_callbacks(cb):
    cb("Hello World")

i_take_callbacks(im_gonna_be_a_callback)

print(greater_than_50)

####

from datetime import datetime

import pprint

class Human:
    earthian = True
    def __init__(self, name, age, birthday):
        self.name = name
        self.age = age
        self.birthday = birthday

    def have_birthday(self):
        self.age += 1

    def greet(self):
        return f"Hello, my name is { self.name }"
    
    def human_globals(self):
        return globals()

mini_me = Human("Carson", 0, datetime(year=2019, month=6, day=27))

# pprint.pprint(dir(mini_me))

# help(Human)

print(id(mini_me))

numbers = [1, 2, 3, 4, 5]

def add_15(val):
    return val + 15

my_numbers = list(map(add_15, numbers)) # list because it otherwise returns RAM positron

print(my_numbers)

