# Dictionaries
# Mutable and unordered
# Represented by key value pairs

my_dictionary = {
    "key": "value",
    "key2": 78
} 
print(my_dictionary)

product = {
    "id": 85787433,
    "description": "submarine",
    "price": 9.99,
    "weight": 9000,
    "department": "grocery",
    "aisle": 3,
    "shelf": "b"
}

print(product["price"])

# Find location and print tuple

location = (product["aisle"], product["shelf"])

print(product.get("quantity"))                      # Get None instead of KeyError
                                                    # None is also False

product["aisle"] = 4                                # to add
product["department"] = "games"                     # to add

for key in product:                                 # in dictionaries, keys are a set
    print(key)

for values in product:                              # to print the values and not the key
    print(product[values])

# A list of the values
print(product.values())

# List of the Keys
print(product.keys())

# Adding to dictionary via Python function
product.update({"whatever": "the value"})

# Creating empty dictionary

empty_dictionary = {}

# Challenge how to add tuple info into new dictionary

data = [ ("name", "your name"), ("age", "your age"), ("class", "Python") ]

for key, value in data:
    empty_dictionary.update({key: value})
print(empty_dictionary)

# Easy way

n_dictionary = {}
n_dictionary.update(data)


