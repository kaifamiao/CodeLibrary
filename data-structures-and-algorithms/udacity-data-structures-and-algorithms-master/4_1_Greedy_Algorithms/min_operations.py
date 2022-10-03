def min_operations(target: int) -> int:
    """
    Returns the number of steps needed to reach the target number,
    assuming that only addition of 1, and doubling of the number is
    possible.
    
    Args:
        target (int): target number
    Returns:
        (int): minimum number of steps required to reach the number
    """
    min_steps = 0
    
    while target > 0:
        while target / 2 == target // 2:
            target = target // 2
            min_steps += 1
        target -= 1
        min_steps += 1
    
    return min_steps


def test_function(test_case):
    target = test_case[0]
    solution = test_case[1]
    output = min_operations(target)
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    target = 18
    solution = 6
    test_case = [target, solution]
    test_function(test_case)
        
    target = 69
    solution = 9
    test_case = [target, solution]
    test_function(test_case)