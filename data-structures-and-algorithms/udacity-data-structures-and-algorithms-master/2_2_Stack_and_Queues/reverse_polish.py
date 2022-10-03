from linked_stack import Stack


def evaluate_postfix(postfix: list) -> int:
    """
    Evaluates and returns the postfix expression.

    Args:
        postfix (list): postfix expression in a list
    Returns:
        int: result of the expression
    """
    stack = Stack()

    for op in postfix:
        if op in ['+', '-', '/', '*']:
            operand2 = int(stack.pop())
            operand1 = int(stack.pop())
            if op == '+':
                stack.push(operand1 + operand2)
            elif op == '-':
                stack.push(operand1 - operand2)
            elif op == '*':
                stack.push(operand1 * operand2)
            elif op == '/':
                stack.push(int(operand1 / operand2))
        else:
            stack.push(op)
    
    return stack.pop()


def test_function(test_case):
    output = evaluate_postfix(test_case[0])
    print(output)
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    test_case_1 = [["3", "1", "+", "4", "*"], 16]
    test_function(test_case_1)

    test_case_2 = [["4", "13", "5", "/", "+"], 6]
    test_function(test_case_2)

    test_case_3 = [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22]
    test_function(test_case_3)
