def heapify(array: list, n: int, i: int) -> None:
    """
    Moves the ith index of the array to its correct heap position.

    Args:
        array (list): array of elements
        n (int): size of the array
        i (int): index
    Returns:
        None
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[left] > array[largest]:
        largest = left
    if right < n and array[right] > array[largest]:
        largest = right
    
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


def heapsort(array: list) -> None:
    """
    Sorts the array in ascending order.

    Args:
        array (list): array of elements
    Returns:
        None
    """
    size = len(array)
    for i in range((size//2)-1, -1, -1):
        heapify(array, size, i)
    
    for i in range(size-1, -1, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, i, 0)


def test_function(test_case):
    heapsort(test_case[0])
    if test_case[0] == test_case[1]:
        print("Pass")
    else:
        print("False")


if __name__ == '__main__':
    arr = [3, 7, 4, 6, 1, 0, 9, 8, 9, 4, 3, 5]
    solution = [0, 1, 3, 3, 4, 4, 5, 6, 7, 8, 9, 9]
    test_case = [arr, solution]
    test_function(test_case)

    arr = [5, 5, 5, 3, 3, 3, 4, 4, 4, 4]
    solution = [3, 3, 3, 4, 4, 4, 4, 5, 5, 5]
    test_case = [arr, solution]
    test_function(test_case)

    arr = [99]
    solution = [99]
    test_case = [arr, solution]
    test_function(test_case)

    arr = [0, 1, 2, 5, 12, 21, 0]
    solution = [0, 0, 1, 2, 5, 12, 21]
    test_case = [arr, solution]
    test_function(test_case)
