def binary_search(array: list, target: int) -> int:
    """
    Returns the index of the target in the array if it is
    present in the array, -1 otherwise.

    Args:
        array (list): sorted array of numbers
        target (int): target number
    Returns:
        int: index of the target
    """
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = right + left // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1

    return -1


def recursive_binary_search(array: list, target: int, left:int, right: int) -> int:
    """
    Returns the index of the target in the array if it is
    present in the array, -1 otherwise.

    Args:
        array (list): sorted array of numbers
        target (int): target number
        left (int): left most index of the array
        right (int): right most index of the array
    Returns:
        int: index of the target
    """
    if left > right:
        return -1

    mid = (right + left) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return recursive_binary_search(array, target, mid+1, right)
    else:
        return recursive_binary_search(array, target, left, mid-1)


def test_function(test_case):
    answer = recursive_binary_search(test_case[0], test_case[1], 0, len(test_case[0]) - 1)
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")


if __name__ == '__main__':
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 6
    index = 6
    test_case = [array, target, index]
    test_function(test_case)
