# Collections

#                       Collections
# Type              Mutable     Ordered     Denotation
# ---------------------------------------------------------
# List              Yes         Yes         [ , ]
# Set               Yes         No          { , }
# Tuple             No          Yes         ( , )
# Dictionary        Yes         No          {key : value,}

# Lists
# Mutable and ordered

names = ["Adam", "Justin", "Xzavier"]

names[0] = "Paul"       # adds Paul at index 0

names.append("Thanos")  # appends Thanos to the end of the list

print(names[-1])        # prints last item (because - zero doesn't exist)

students = [
    "",
    "Steve Rogers",
    "Tony Stark",
    "Thor",
    "Natasha Romanoff",
    "Hawkeye",
]

contains_anything = [
    "string",
    6,
    2 + 2j,
    [
        "nested strings"
    ]
]

name_list  = students.extend(names)        # combines lists together
names.pop()                                # removes last by default
students.remove("Natasha Romanoff")        # removes item

start_stop_step_list = students[0:3:1]     # means start[0], stop[3], step[1]

reversed_list = students[::-1]             # reverses at [-1]

reversed_again = reversed(students)        # fx reversed() that does the same

students[1].lower()                        # makes index[0] lowercase

every_other_student = students[::2]        # returns every other student

# Tuples
# Immutable and ordered

my_tuple = (12, 32)

my_tuple[0]                         # can be accessed by index

my_name = ("Paul", "Adam", "Xzavier", "Justin")

leaders = my_name[1:4]

print(leaders)                      # index is NON INCLUSIVE

tester = ("John",)                  # comma must be added or Python will break Tuple

# Sets
# Mutable and unordered
# Unique items ONLY - duplicates will not add

states = {"Indiana", "Illinois", "Michigan"}
states.add("Iowa")

print("Michigan" in states)         # results in Boolean True

states.remove("Indiana")            # remove with KeyValue Error if not found
states.discard("Alaska")            # remove - no error if not found

sentence = "Mary had a little lamb."

list_of_words = sentence.split()    # splits words in a sentence

print(list(sentence))               # list() makes a list of every letter

# Dictionary
# Mutable and unordered
# Consists of key value pairs

my_dictionary = {
    "name": "Adam Jayne",
    "age":  25
}

my_dictionary["name"]                               # grab value at 'name' key
my_dictionary.get("name")                           # get value of 'name' key
my_dictionary["name"] = "Paul Niemczyk"             # update value at 'name' key
my_dictionary["hobby"] = "Python"                   # add kvp if key doesn't
my_dictionary.update({"hobby": "Golf", "age": 28})  # add/update

my_dictionary.keys()                                # gets key in dict
my_dictionary.values()                              # gets value in dict
my_dictionary.items()                               # gets items in dict

