# Conditionals
# conditional that resolves to a boolean statement

left = True
right = False

right != "train"

# Equality Operators

left != right # left and right are not equivalent
left == right # left and reight are equivalent
left is right # left and right are the same identity
left is not right # left and right are not the same identity

# Comparison operators

age_1 = 23
age_2 = 45

age_1 > age_2 # left is greater than right
age_1 < age_2
age_1 >= age_2
age_1 <= age_2

# Logical Operators

# and operator checks if both are True
# or operator means either has to be True
# not operator swaps True statement into False

# a     b       a and b
#----------------------
# True   True    True
# True   False   False
# False  True    False
# False  False   False

# a     b       a or b
# ---------------------
# True  True    True
# True  False   True
# False True    True
# False False   False

# a     not a
#-------------
# True  False
# False True

x = 1
name = "Ryan"

if x > 3 and name == "Ryan":
    print("x is pretty big, and that persons name is Ryan")
elif x <= 3:
    print("Maybe x is big, I dunno")
else:
    print("Otherwise, no")

# Challenge
# Take a name and age, and if the person is under 18, say 'Name, you are not an adult'.
# if the person is 18 but not 21, say 'you are  an adult, but not quite yet
# IF THE PERSON IS 21 and older, say 'You are an adult'

name = input("What is your name? ")
age = input("How old are you? ")
int_age = int(age)
first_letter = name[0]

if first_letter == 'P':
    print('Cool name!')

if int_age <= 18:
    print('You are not an adult')
elif int_age >= 18 and int_age < 21:
    print('You are an adult, but not quite yet')
else:
        print('You are an adult')

you = "Person"
new_you = you.replace("r", "f")
print(new_you)

if name[0].lower() == "a":
    print('Cool Name!')

"""
Challenge

# Declare a number
# If number divisible by 3, print 'Fizz'
# If number divisible by 5, print 'Buzz'
# If number divisible by 3 and 5, print 'Fizzbuzz'
# Otherwise, just print the number

# Test cases: 1, 3, 5, 10, 15, 98
"""

number = int(input("Give me a number in range 0-100: "))

if number % 3 == 0 and number % 5 == 0:
    print("Fizzbuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)

# Can use least common denominator to  hange line 102 into: if number % 15 == 0