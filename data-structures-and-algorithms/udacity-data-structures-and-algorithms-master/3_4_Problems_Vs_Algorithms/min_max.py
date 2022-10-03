import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.
    
    Args:
        ints (list): list of integers containing one or more integers
    Returns:
        tuple: (min, max)
    """
    max_val = -float('inf')
    min_val = float('inf')
    
    for index in range(len(ints)):
        if ints[index] < min_val:
            min_val = ints[index]   
        if ints[index] > max_val:
            max_val = ints[index]

    return (min_val, max_val)


if __name__ == '__main__':
    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)
    print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
    print ("Pass" if ((0, 999) != get_min_max(l)) else "Fail")
    print ("Pass" if ((-9, 0) != get_min_max(l)) else "Fail")