# Bubble Sort Algorithm

def bubble_sort(numbers):
    swapped = True

    while swapped:
        swapped = False
        for i in range(len(numbers) - 1):   # -1 range non-inclusive
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True

# Algorithm testing

my_list = [5 , 2, 90, 6, 32]

bubble_sort(my_list)

print(my_list)