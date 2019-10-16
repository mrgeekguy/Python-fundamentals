# Recursion

my_items = [1, 2, 3, 6, 89]

def recursive_sum(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + recursive_sum(numbers[1:])
print(recursive_sum(my_items))
print(sum(my_items))

# Fibonacci sequence
# Rules:
# Start with 0 and 1
# New number = sum of previous two

def fib(numbers, current = 1, previous = 0, count = 0):
    if count < numbers:
        return fib(numbers, current + previous, current, count + 1)
    else:
        return current

print(fib(4))


