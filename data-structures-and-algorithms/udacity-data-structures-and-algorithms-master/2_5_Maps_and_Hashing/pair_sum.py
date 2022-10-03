def pair_sum(input_list: list, target: int) -> list:
    """
    Returns indices of the pair of elements in input list that
    sum up to the given target.

    Args:
        input_list (list): List of numbers.
        target (int): Target sum.
    Returns:
        list: Indices of elements that sum up to target.
    """
    hash_table = dict()
    for i, elem in enumerate(input_list):
        if (target - elem) in hash_table:
            return [hash_table[target-elem], i]
        else:
            hash_table[elem] = i


def test_function(test_case):
    output = pair_sum(test_case[0], test_case[1])
    print(output)
    if sorted(output) == test_case[2]:
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    test_case_1 = [[1, 5, 9, 7], 8, [0, 3]]
    test_function(test_case_1)

    test_case_2 = [[10, 5, 9, 8, 12, 1, 16, 6], 16, [0, 7]]
    test_function(test_case_2)

    test_case_3 = [[0, 1, 2, 3, -4], -4, [0, 4]]
    test_function(test_case_3)