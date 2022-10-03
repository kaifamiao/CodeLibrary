def __swap(array: list, x: int, y: int) -> None:
    """Swaps x and y position of the array."""
    temp = array[x]
    array[x] = array[y]
    array[y] = temp


def __quick_sort(array: list, left: int, right: int) -> None:
    """Driver function for quick sort."""
    if left >= right:
        return
    else:
        pivot = array[right]
        lo = left
        hi = right - 1
        while True:
            while array[lo] <= pivot:
                if lo == right:
                    break
                lo += 1
            while array[hi] > pivot:
                if hi == left:
                    break
                hi -= 1
            if lo >= hi:
                break
            __swap(array, lo, hi)
        __swap(array, lo, right)
        __quick_sort(array, left, lo-1)
        __quick_sort(array, lo+1, right)


def sort(array: list) -> None:
    """
    Sorts the array in ascending order.

    Args:
        array (list): array of elements
    Returns:
        None
    """
    __quick_sort(array, 0, len(array)-1)


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
