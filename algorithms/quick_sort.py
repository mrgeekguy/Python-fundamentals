# Quick Sort

def partition(numbers, low, high):

    pivot = numbers[(low + high) // 2]

    i = low - 1
    j = high + 1

    while True:
        i += 1

        while numbers[i] < pivot:
            i += 1
            
        j -= 1
        while numbers[j] > pivot:
            j -= 1

        if i >= j:
            return j

    numbers[i], numbers[j] = numbers[j], numbers[i]

def quick_sort(numbers):

    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    
    _quick_sort(numbers, 0, len(numbers) - 1)