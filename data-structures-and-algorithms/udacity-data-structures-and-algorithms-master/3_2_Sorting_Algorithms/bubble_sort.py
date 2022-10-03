def sort(array: list) -> None:
    """
    Sorts the array in ascending order.

    Args:
        array (list): array of elements
    Returns:
        None
    """
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp


if __name__ == '__main__':
    array1 = [2, 13, 1, 14, 6]
    array2 = []
    array3 = [112, 13]

    sort(array1)
    sort(array2)
    sort(array3)

    print(' '.join([str(i) for i in array1]))
    print(' '.join([str(i) for i in array2]))
    print(' '.join([str(i) for i in array3]))

