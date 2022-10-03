def duplicate_number(array: list) -> int:
    """
    Finds any duplicate number in the array.

    Args:
        array (list): list of numbers.
    Returns:
        int: duplicate number.
    """
    for i in array:
        if array.count(i) == 2:
            return i


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    output = duplicate_number(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    arr = [0, 0]
    solution = 0
    test_case = [arr, solution]
    test_function(test_case)

    arr = [0, 2, 3, 1, 4, 5, 3]
    solution = 3
    test_case = [arr, solution]
    test_function(test_case)

    arr = [0, 1, 5, 4, 3, 2, 0]
    solution = 0
    test_case = [arr, solution]
    test_function(test_case)

    arr = [0, 1, 5, 5, 3, 2, 4]
    solution = 5
    test_case = [arr, solution]
    test_function(test_case)
