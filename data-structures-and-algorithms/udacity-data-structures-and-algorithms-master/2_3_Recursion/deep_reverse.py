def deep_reverse(array: list) -> list:
    """
    Reverses the given list. If the given list contains a list,
    it is also reversed.
    """
    if type(array) is not list:
        return array
    else:
        return [deep_reverse(elem) for elem in array[::-1]]


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = deep_reverse(arr)
    if output == solution:
        print("Pass")
    else:
        print("False")


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    solution = [5, 4, 3, 2, 1]
    test_case = [arr, solution]
    test_function(test_case)

    arr = [1, 2, [3, 4, 5], 4, 5]
    solution = [5, 4, [5, 4, 3], 2, 1]
    test_case = [arr, solution]
    test_function(test_case)

    arr = [1, [2, 3, [4, [5, 6]]]]
    solution = [[[[6, 5], 4], 3, 2], 1]
    test_case = [arr, solution]
    test_function(test_case)

    arr =  [1, [2,3], 4, [5,6]]
    solution = [ [6,5], 4, [3, 2], 1]
    test_case = [arr, solution]
    test_function(test_case)