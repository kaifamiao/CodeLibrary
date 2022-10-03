class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def skip_i_delete_j(head: Node, i: int, j: int) -> None:
    """
    Skips first i nodes of a linked list, then delete next j nodes,
    and continues until it reaches the end.

    Args:
        head (Node): head of the linked list.
        i (int): Nodes to be skipped.
        j (int): Nodes to be deleted.
    Returns:
        None
    """
    counter = 0
    placeholder = head

    while placeholder is not None:
        if counter < i:
            placeholder = placeholder.next
            counter = (counter + 1) % (i + j)
        else:
            if placeholder is head:
                placeholder = placeholder.next
                head = placeholder
            else:
                temp = head
                while temp.next is not placeholder:
                    temp = temp.next
                temp.next = placeholder.next
                placeholder = placeholder.next
            counter = (counter + 1) % (i + j)
    
    return head


# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

def test_function(test_case):
    head = test_case[0]
    i = test_case[1]
    j = test_case[2]
    solution = test_case[3]
        
    temp = skip_i_delete_j(head, i, j)
    index = 0
    try:
        while temp is not None:
            if temp.data != solution[index]:
                print("Fail")
                return
            index += 1
            temp = temp.next
        print("Pass")
    except Exception as e:
        print("Fail")


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    i = 2
    j = 2
    head = create_linked_list(arr)
    solution = [1, 2, 5, 6, 9, 10]
    test_case = [head, i, j, solution]
    test_function(test_case)

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    i = 2
    j = 3
    head = create_linked_list(arr)
    solution = [1, 2, 6, 7, 11, 12]
    test_case = [head, i, j, solution]
    test_function(test_case)

    arr = [1, 2, 3, 4, 5]
    i = 2
    j = 4
    head = create_linked_list(arr)
    solution = [1, 2]
    test_case = [head, i, j, solution]
    test_function(test_case)