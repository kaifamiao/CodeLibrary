from linked_stack import Stack
from array_queue import Queue


def reverse_queue(queue: Queue) -> Queue:
    """
    Reverse and returns the given queue.

    Args:
        queue (Queue): Queue to be reversed.
    Returns:
        Queueu: Reversed queue.
    """
    stack = Stack()
    while not queue.is_empty():
        stack.push(queue.dequeue())
    while not stack.is_empty():
        queue.enqueue(stack.pop())
    return queue


def test_function(test_case):
    queue = Queue()
    for num in test_case:
        queue.enqueue(num)
    
    reverse_queue(queue)
    index = len(test_case) - 1
    while not queue.is_empty():
        removed = queue.dequeue()
        if removed != test_case[index]:
            print("Fail")
            return
        else:
            index -= 1
    print("Pass")


if __name__ == '__main__':
    test_case_1 = [1, 2, 3, 4]
    test_function(test_case_1)

    test_case_2 = [1]
    test_function(test_case_2)
