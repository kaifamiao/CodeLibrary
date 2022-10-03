from binary_search import binary_search


def first_and_last_index(source: list, target: int):
    """
    Returns the first and last index of the target in source array.

    Args:
        source (list): array of elements
        target (int): target element
    Returns:
        list: [first index, last index]
    """
    index = binary_search(source, target)
    if index == -1:
        return [-1, -1]
    
    first_index = index
    while source[first_index] == target:
        if first_index == 0:
            break
        if source[first_index - 1] == target:
            first_index -= 1
        else:
            break
    
    last_index = index
    while source[last_index] == target:
        if last_index == len(source) - 1:
            break
        if source[last_index + 1] == target:
            last_index += 1
        else:
            break
    
    return [first_index, last_index]



def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    solution = test_case[2]
    output = first_and_last_index(input_list, number)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    input_list = [1]
    number = 1
    solution = [0, 0]
    test_case_1 = [input_list, number, solution]
    test_function(test_case_1)

    input_list = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6]
    number = 3
    solution = [3, 6]
    test_case_2 = [input_list, number, solution]
    test_function(test_case_2)

    input_list = [0, 1, 2, 3, 4, 5]
    number = 5
    solution = [5, 5]
    test_case_3 = [input_list, number, solution]
    test_function(test_case_3)

    input_list = [0, 1, 2, 3, 4, 5]
    number = 6
    solution = [-1, -1]
    test_case_4 = [input_list, number, solution]
    test_function(test_case_4)
