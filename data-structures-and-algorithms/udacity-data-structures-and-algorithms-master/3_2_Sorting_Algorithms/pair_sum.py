from quick_sort import sort


def pair_sum(array: list, target: int) -> tuple:
    """
    Returns tuple of numbers from the array that sum up to the
    given target.

    Args:
        array (list): list of numbers
        target (int): target
    Returns:
        tuple: (first number, second number)
    """
    sort(array)
    i = 0
    j = len(array) - 1
    while i <= j:
        if array[i] + array[j] == target:
            return [array[i], array[j]]
        elif array[i] + array[j] > target:
            j -= 1
        elif array[i] + array[j] < target:
            i +=1
    return [None, None]


def test_function(test_case):
    input_list = test_case[0]
    target =test_case[1]
    solution = test_case[2]
    output = pair_sum(input_list, target)
    if output == solution:
        print("Pass")
    else:
        print("False")


if __name__ == '__main__':
    input_list = [2, 7, 11, 15]
    target = 9
    solution = [2, 7]
    test_case = [input_list, target, solution]
    test_function(test_case)

    input_list = [0, 8, 5, 7, 9]
    target = 9
    solution = [0, 9]
    test_case = [input_list, target, solution]
    test_function(test_case)

    input_list = [110, 9, 89]
    target = 9
    solution = [None, None]
    test_case = [input_list, target, solution]
    test_function(test_case)
