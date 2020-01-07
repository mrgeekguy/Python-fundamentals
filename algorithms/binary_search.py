# Binary Search Algorithm

def binary_search(numbers, item):
    first = 0
    last = len(numbers) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if numbers[midpoint] == item:
            found = True
        else:
            if item < numbers[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found

my_list = [1, 2, 3, 4, 5, 6, 7]

print(binary_search(my_list, 5))

print(*my_list, sep= "\n")