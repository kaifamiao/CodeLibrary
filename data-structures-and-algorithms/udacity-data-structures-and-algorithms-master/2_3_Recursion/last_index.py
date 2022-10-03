def last_index(array: list, target: int) -> int:
    """
    Returns the last index of the target in the array.
    Returns -1 if target is not present in the array.
    """
    if len(array) == 0:
        return -1
    elif len(array) == 1:
        return 0 if array[0] == target else -1
    else:
        previous_index = last_index(array[1:], target)
        if array[0] != target and previous_index == -1:
            return -1
        else:
            return previous_index + 1


def test_function(test_case):
    arr = test_case[0]
    target = test_case[1]
    solution = test_case[2]
    output = last_index(arr, target)
    if output == solution:
        print("Pass")
    else:
        print("False")


if __name__ == '__main__':
    arr = [1, 2, 5, 5, 4]
    target = 5
    solution = 3
    test_case = [arr, target, solution]
    test_function(test_case)

    arr = [1, 2, 5, 5, 4]
    target = 7
    solution = -1
    test_case = [arr, target, solution]
    test_function(test_case)

    arr = [91, 19, 3, 8, 9]
    target = 91
    solution = 0
    test_case = [arr, target, solution]
    test_function(test_case)

    arr = [1, 1, 1, 1, 1, 1]
    target = 1
    solution = 5
    test_case = [arr, target, solution]
    test_function(test_case)
