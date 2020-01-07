# Insertion Sort Algorithm

def insertion_sort(numbers):

    for i in range(1, len(numbers)):
        item_to_insert = numbers.pop(i)
        j = i - 1

        while j >= 0 and numbers[j] > item_to_insert:
            j -= 1
        
        numbers.insert(j + 1, item_to_insert)

# Testing

my_numbers = [8, 3, 12, 88]

insertion_sort(my_numbers)

print(my_numbers)

for i in range(1, len(my_numbers)):
    print(i)
