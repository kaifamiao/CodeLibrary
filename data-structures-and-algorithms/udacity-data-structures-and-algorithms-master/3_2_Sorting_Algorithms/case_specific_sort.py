def __merge(array: list, left: int, mid: int, right: int) -> None:
    """
    Merges two sorted region of an array into an combined sorted region.

    Args:
        array (list): array of elements
        left (int): starting index of first region
        mid (int): last index of first region
        right (int): last index of right region
    Returns:
        None
    """
    size = right - left + 1
    temp = [None for _ in range(size)]

    first = left
    second = mid + 1
    for i in range(size):
        if first > mid:
            temp[i] = array[second]
            second += 1
        elif second > right:
            temp[i] = array[first]
            first += 1
        elif array[first] < array[second]:
            temp[i] = array[second]
            second += 1
        else:
            temp[i] = array[first]
            first += 1

    for i in range(size):
        array[left+i] = temp[i]


def __merge_sort(array: list, left: int, right: int):
    """
    Driver function for merge sort.
    """
    size = right - left + 1
    if size <= 1:
        return
    else:
        mid = (right + left) // 2
        __merge_sort(array, left, mid)
        __merge_sort(array, mid+1, right)
        __merge(array, left, mid, right)


def sort(array: list) -> None:
    """
    Sorts the array in ascending order.

    Args:
        array (list): array of elements
    Returns:
        None
    """
    __merge_sort(array, 0, len(array)-1)


def case_sort(string: str) -> None:
    """
    Sorts given string but keeps position of upper and lower
    cases intact.

    Args:
        string (str): string to be sorted
    Returns:
        None
    """
    lower = []
    upper = []
    for char in string:
        if ord(char) < 91:
            upper.append(char) 
        else:
            lower.append(char)
    
    sort(lower)
    sort(upper)

    output = ''
    for char in string:
        if ord(char) < 91:
            output += upper.pop() 
        else: 
            output += lower.pop()
    
    print(output)
    return output


def test_function(test_case):
    test_string = test_case[0]
    solution = test_case[1]
    
    if case_sort(test_string) == solution:
        print("Pass")
    else:
        print("False")


if __name__ == '__main__':
    test_string = 'fedRTSersUXJ'
    solution = "deeJRSfrsTUX"
    test_case = [test_string, solution]
    test_function(test_case)

    test_string = "defRTSersUXI"
    solution = "deeIRSfrsTUX"
    test_case = [test_string, solution]
    test_function(test_case)