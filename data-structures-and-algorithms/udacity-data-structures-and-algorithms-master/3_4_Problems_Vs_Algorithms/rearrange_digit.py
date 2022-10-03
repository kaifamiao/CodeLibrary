def sort(array: list, left, right):
    """
    Sorts array in descending order using quicksort algorithm.
    """
    if left < right:
        pivot = array[right]
        start = left
        end = right - 1
        while True:
            while start < right and array[start] > pivot:
                start += 1
            while end >= left and array[end] <= pivot:
                end -= 1
            if start >= end:
                break
            array[start], array[end] = array[end], array[start]
        array[start], array[right] = array[right], array[start]
        sort(array, left, start-1)
        sort(array, start+1, right)


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sort(input_list, 0, len(input_list)-1)
    number1 = []
    number2 = []
    sentinel = True
    for i  in input_list:
        if sentinel:
            number1.append(i)
            sentinel = not sentinel
        else:
            number2.append(i)
            sentinel = not sentinel

    return [int(''.join([str(i) for i in number1])), int(''.join([str(i) for i in number2]))]    


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    test_function([[1, 2, 3, 4, 5], [542, 31]])
    test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
