from binary_search import binary_search


def find_first(target: int, source: list) -> int:
    """
    Returns the first occurance of target in the source if there
    are multiple targets.

    Args:
        target (int): target element
        source (list): sorted array of elements
    Returns:
        int: first occurance of element, -1 otherwise
    """
    index = binary_search(source, target)
    if index == -1:
        return None
    while source[index] == target:
        if index == 0:
            return 0
        if source[index - 1] == target:
            index -= 1
        else:
            return index


def contains(target: int, source:list) -> bool:
    """
    Checks if the target is present in the source.

    Args:
        target (int): target element
        source (list): sorted array of elements
    Returns:
        bool: True if the element is in the array, False otherwise
    """
    return binary_search(source, target) != -1
