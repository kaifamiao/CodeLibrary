def add_one(input_list: list) -> list:
    """
    Adds one to number given as a list.

    Args:
        input_list (list): integer given as a list.
    Returns:
        list: given integer plus one as a list.
    """
    output_list = []
    # in the first loop, carry works as number to be added.
    # from the next, it works like actual carry.
    carry = 1
    
    for digit in input_list[::-1]:
        dig_sum = digit + carry
        output_list.append(dig_sum % 10)
        carry = int(dig_sum / 10)
    
    if carry != 0:
        output_list.append(carry)
    
    return output_list[::-1]


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = add_one(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass")

if __name__ == '__main__':
    arr = [0]
    solution = [1]
    test_case = [arr, solution]
    test_function(test_case)

    arr = [1, 2, 3]
    solution = [1, 2, 4]
    test_case = [arr, solution]
    test_function(test_case)

    arr = [9, 9, 9]
    solution = [1, 0, 0, 0]
    test_case = [arr, solution]
    test_function(test_case)
