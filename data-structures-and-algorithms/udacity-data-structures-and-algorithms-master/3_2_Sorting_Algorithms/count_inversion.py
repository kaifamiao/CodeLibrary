def __merge(array: list, left: int, mid: int, right: int) -> int:
    """
    Merges two sorted region of an array into an combined sorted region,
    and returns the number of inversions.

    Args:
        array (list): array of elements
        left (int): starting index of first region
        mid (int): last index of first region
        right (int): last index of right region
    Returns:
        int: number of inversions
    """
    size = right - left + 1
    temp = [None for _ in range(size)]
    inv = 0

    first = left
    second = mid + 1
    for i in range(size):
        if first > mid:
            temp[i] = array[second]
            second += 1
        elif second > right:
            temp[i] = array[first]
            first += 1
        elif array[first] > array[second]:
            temp[i] = array[second]
            second += 1
            inv += 1
        else:
            temp[i] = array[first]
            first += 1

    for i in range(size):
        array[left+i] = temp[i]
    return inv

def __merge_sort(array: list, left: int, right: int):
    """
    Driver function for merge sort.
    """
    size = right - left + 1
    if size <= 1:
        return 0
    else:
        mid = (right + left) // 2
        left_inv = __merge_sort(array, left, mid)
        right_inv = __merge_sort(array, mid+1, right)
        inv = __merge(array, left, mid, right)
        return left_inv + right_inv + inv


def inversions(array: list) -> int:
    """
    Counts the number of inversions in the array.

    Args:
        array (list): array of elements
    Returns:
        int: total number of inversions
    """
    return __merge_sort(array, 0, len(array)-1)


if __name__ == '__main__':
    array1 = [2, 13, 1, 14, 6]
    array2 = []
    array3 = [112, 13]

    inv1 = inversions(array1)
    inv2 = inversions(array2)
    inv3 = inversions(array3)

    print(str(inv1))
    print(str(inv2))
    print(str(inv3))