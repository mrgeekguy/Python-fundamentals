# Collections

# List
# CRUD
# Create, read, update, delete

my_list = [2, 4, 3]                 # create
first_item = my_list[0]             # read - indexing
my_slice = my_list[1:3]             # read - slicing # stop is non-inclusive 
my_list.append(["hello", "world"])  # update - appends to the end
my_list[3][1]                       # read - nested lists
my_list[1] = 6                      # udpate - index
print(my_list)
my_list.insert(1, 8)                # update - at (index, object_to_place)
print(my_list)
my_list.pop()                       # update - popping the last item off list unless specified
my_list.extend(["hello", "world"])  # update - combining lists together
my_list.remove("Hello")             # update - remove first value found
my_list.clear()                     # update - remove all items from a list

del my_list                         # delete - remove the list from memory

# Loops
# ability to iterate over an iterable or until a condition is False

# For loop
# for <something> in <iterable>:

for i in range(10):
    x = i + i                       # shared scope with the file or where declared
    if i >= 7:
        break                       # break will end the loop
    if i > 8:
        continue                    # continue will go to the next iteration
    a = i + i

# While loop
# while a condition has been met, do this code
# while <condition> True:

n = 8
while n >= 0:
    print("Not yet")
    n -= 1
print("finally done")

# Dictionary
# key value collection, unordered and mutable

my_dictionary = {
    "name": "Adam Jayne",
    "age":  25
}

my_dictionary["name"]                               # grab value at 'name' key
my_dictionary.get("name")                           # get value of 'name' key
my_dictionary["name"] = "Paul Niemczyk"             # update value at 'name' key
my_dictionary["hobby"] = "Python"                   # add kvp if key doesn't
my_dictionary.update({"hobby": "Golf", "age": 28})  # add/update

my_dictionary.keys()
my_dictionary.values()
my_dictionary.items()

# parameter for construct; argument for actual data

# Classes
# custom data type containing methods and attributes (values)

class Animal:
    
    def __init__(self, kingdom):
        self.kingdom = kingdom
    
    def get_kingdom(self):
        return self.kingdom

class Human(Animal):

    def __init__(self, kingdom, name, age):
        super().__init__(kingdom)
        self.name = name
        self.age = age

    def speak(self):
        return f"Hello, I am :{ self.name }"

me = Human("Camelot", "Adam", 25)

print(me.get_kingdom())