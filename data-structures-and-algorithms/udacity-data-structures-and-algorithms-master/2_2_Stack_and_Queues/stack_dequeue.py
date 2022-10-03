from linked_stack import Stack


def stack_dequeue(stack: Stack) -> any:
    """
    Dequeues an element from the stack.

    Args:
        stack (Stack): the stack.
    Returns:
        any: value of the bottom element of the stack.
    """
    s1 = Stack()
    s2 = Stack()

    for i in range(stack.size() - 1):
        s1.push(stack.pop())
    for i in range(s1.size()):
        s2.push(s1.pop())
    
    bottom = stack.pop()
    stack = s2
    return bottom.value

