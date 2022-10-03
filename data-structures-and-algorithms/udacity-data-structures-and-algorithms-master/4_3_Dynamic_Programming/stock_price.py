def max_returns(arr: list) -> int:
    """
    Returns the maximum profit possible from the stock price at different times.

    Args:
        arr (list): stock prices over times
    Returns:
        int: maximum profit
    """
    if len(arr) < 2:
        return
    
    min_index = 0
    max_index = 1
    current_min_index = 0

    for i in range(1, len(arr)):
        if arr[i] < arr[current_min_index]:
            current_min_index = i
        if arr[max_index] - arr[min_index] < arr[i] - arr[current_min_index]:
            max_index = i
            min_index = current_min_index

    return arr[max_index] - arr[min_index]
        

def test_function(test_case):
    prices = test_case[0]
    solution = test_case[1]
    output = max_returns(prices)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    prices = [2, 2, 7, 9, 9, 12, 18, 23, 34, 37, 45, 54, 78]
    solution = 76
    test_case = [prices, solution]
    test_function(test_case)

    prices = [54, 18, 37, 9, 11, 48, 23, 1, 7, 34, 2, 45, 67]
    solution = 66
    test_case = [prices, solution]
    test_function(test_case)

    prices = [78, 54, 45, 37, 34, 23, 18, 12, 9, 9, 7, 2, 2]
    solution = 0
    test_case = [prices, solution]
    test_function(test_case)
