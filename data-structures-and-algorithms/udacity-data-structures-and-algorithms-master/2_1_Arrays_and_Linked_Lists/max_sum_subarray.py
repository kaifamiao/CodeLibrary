def max_sum_subarray(array: list) -> int:
    """
    Returns the maximum sum of contiguous subarrays of a given array
    using Kadane's Algorithm.

    Args:
        array (list): list of numbers.
    Returns:
        int: maximum sum of a contiguous subarray.
    """
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    
    max_global = array[0]
    max_current = array[0]

    for i in range(1, len(array)):
        max_current = max(array[i], max_current + array[i])
        if max_current > max_global:
            max_global = max_current
    
    return max_global


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = max_sum_subarray(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    arr= [1, 2, 3, -4, 6]
    solution= 8 # sum of array
    test_case = [arr, solution]
    test_function(test_case)

    arr = [1, 2, -5, -4, 1, 6]
    solution = 7   # sum of last two elements
    test_case = [arr, solution]
    test_function(test_case)

    arr = [-12, 15, -13, 14, -1, 2, 1, -5, 4]
    solution = 18  # sum of subarray = [15, -13, 14, -1, 2, 1]
    test_case = [arr, solution]
    test_function(test_case)
