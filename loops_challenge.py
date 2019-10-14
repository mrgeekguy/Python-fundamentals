puzzle = open("frequencies.txt", "r").read().split("\n")
# name of file to open in the same folder
# r stands for read only
# .split() splits the string into new lines \n

numbers = [ int(i) for i in puzzle ] # list comprehension creates list from a for loop

''' another way to do the above

numbers = []
for i in puzzle:
    numbers.append(int(i))

'''
# What is the final frequency?
# Do with for loop
# while loop
# python built-in function

# for loop

frequency = 0

for i in numbers: 
    frequency += i
print(frequency)

# while loop

x = 0 # tracks index
frequency = 0 # tracks the sum(numbers)

while x < len(numbers): # makes sure the index stops on last of numbers
    frequency += numbers[x] 
    x += 1
print(frequency)


# python built-in

total = sum(numbers)
print(total)



