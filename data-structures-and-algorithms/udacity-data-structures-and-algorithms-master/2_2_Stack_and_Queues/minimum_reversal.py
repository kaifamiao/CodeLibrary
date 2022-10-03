from linked_stack import Stack


def minimum_bracket_reversals(input_string: str) -> int:
    """
    Returns the minimum number of reversals required to balance
    the brackets.

    Args:
        input_string (str): input string of brackets.
    Returns:
        int: minimum number of reversals to balance brackets. -1
             if can not be balanced.
    """
    if len(input_string) % 2 != 0:
        return -1
    
    extra_reversals = 0
    if input_string[0] == '}':
        input_string = '{' + input_string
        extra_reversals += 1
    if input_string[-1] == '{':
        input_string = input_string + '}'
        extra_reversals += 1
    
    stack = Stack()
    for char in input_string:
        if char == '}':
            if stack.top() == '{':
                _ = stack.pop()
            else:
                stack.push(char)
        else:
            stack.push(char)

    return int(stack.size() / 2) + extra_reversals


if __name__ == '__main__':
    # Case 1
    test_case_1 = ["}}}}", 2]
    print('Case 1 is :{}'.format(minimum_bracket_reversals(test_case_1[0])))

    # Case 2
    test_case_2 = ["}}{{", 2]
    print('Case 2 is :{}'.format(minimum_bracket_reversals(test_case_2[0])))


    # Case 3
    test_case_3 = ["{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}", 13]
    print('Case 3 is :{}'.format(minimum_bracket_reversals(test_case_3[0])))

    # Case 4
    test_case_4 = ["}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{", 2]
    print('Case 4 is :{}'.format(minimum_bracket_reversals(test_case_4[0])))

    # Case 5
    test_case_5 = ["}}{}{}{}{}{}{}{}{}{}{}{}{}{}{}", 1]
    print('Case 5 is :{}'.format(minimum_bracket_reversals(test_case_5[0])))