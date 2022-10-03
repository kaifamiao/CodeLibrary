from linked_stack import Stack

def check_equation(eq: str) -> bool:
    """
    Checks if the parentheses in the given equation is balanced or not.

    Args:
        eq (str): equation
    Returns:
        bool: True if equation is valid, False otherwise.
    """
    stack = Stack()
    for elem in eq:
        if elem == '(':
            stack.push(elem)
        elif elem == ')':
            if stack.pop() is None:
                return False
    
    if stack.size() == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print ("Pass" if (check_equation('((3^2 + 8)*(5/2))/(2+6)')) else "Fail")
    print ("Pass" if not (check_equation('((3^2 + 8)*(5/2))/(2+6))')) else "Fail")
        