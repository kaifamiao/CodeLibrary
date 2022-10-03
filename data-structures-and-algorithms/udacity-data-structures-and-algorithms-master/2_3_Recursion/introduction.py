def sum_integers(n: int) -> int:
    """
    Returns the sum of all integers from 1 to n.
    """
    if n == 1:
        return 1
    else:
        return n + sum_integers(n - 1)


def sum_array(array: list, idx: int) -> int:
    """
    Returns the sum of the integers in the array.
    """
    if len(array) - 1 == idx:
        return array[idx]
    else:
        return array[idx] + sum_array(array, idx + 1)


if __name__ == '__main__':
    print(sum_array([1,2,3,4,5,6,7,8,9,10], 0))