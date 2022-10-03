def find_pivot(array: list, left: int, right: int):
    """
    Finds and returns the index of the pivot in a rotated
    sorted array.
    """
    while left <= right:
        mid = (right + left) // 2
        if mid < right and array[mid] > array[mid + 1]:
            return mid
        if mid > left and array[mid] < array[mid - 1]:
            return mid - 1
        if array[left] <= array[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search(array, target, left, right):
    while left <= right:
        mid = (right + left) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    pivot = find_pivot(input_list, 0, len(input_list)-1)
    if pivot == -1:
        return binary_search(input_list, number, 0, len(input_list)-1)
    if input_list[pivot] == number:
        return pivot
    if input_list[0] <= number:
        return binary_search(input_list, number, 0, pivot - 1)
    else:
        return binary_search(input_list, number, pivot+1, len(input_list)-1)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])