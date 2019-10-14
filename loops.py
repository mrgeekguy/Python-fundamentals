# Loops
# Two types: For and While

# For loop

animals = ["Jaguar", "Colts", "Racoons", "Fox", "Cat", "Toucan"]

for animal in animals:              # animal is a variable here
    print(animal)

for i in range(1, 11):
    print(i)
    """ Fizzbuzz logic here """

for i in range(30):                 # "j" has to execute 30 times before "i" executes once
    for j in range(1, 30, -1):      # Executed a total of 900 times
        if i == j:
            print("They match")

expenses = [
    ("McDonalds", 12.00),
    ("Steam", 49.99),
    ("Rent", 900.00)
]

total = 0

for expense in expenses:
    total += expense[1]
print(total)

# While Loop

while False:
    # code block
    print("I'm in a while loop")

x = 0

while x < 100:
    print(x)
    x += 4

# Challenge

products = ["nvidia", "amd", "arm", "intel", "risc"]
search_term = 'amd'
x = 0

while x < len(products) and search_term != products[x]:
    x += 1
else:
    print("Found search term")
    print("x")

# simplified

if search_term in products:
    print(products.index(search_term))


