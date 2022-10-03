def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    zero_index = 0
    two_index = len(input_list) - 1
    counter = 0

    while counter <= two_index:
        if input_list[counter] == 0:
            input_list[zero_index], input_list[counter] = input_list[counter], input_list[zero_index]
            zero_index += 1
            counter += 1
        elif input_list[counter] == 2:
            input_list[two_index], input_list[counter] = input_list[counter], input_list[two_index]
            two_index -= 1
        else:
            counter += 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])