def _staircase(n: int, cache: list) -> int:
    if cache[n] is not None:
        return cache[n]
    elif n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        total_ways = 0
        total_ways += _staircase(n - 1, cache)
        total_ways += _staircase(n - 2, cache)
        total_ways += _staircase(n - 3, cache)
        if cache[n] is None:
            cache[n] = total_ways
        return total_ways


def staircase(n:int) -> int:
    """
    Returns the total number of possible ways to climb n staircases
    assuming that one can take 1, 2, or 3 steps.

    Args:
        n (int): Number of staircases.
    Returns:
        int: Total possible ways to climb the staircases.
    """
    CACHE = [None for _ in range(n + 1)]
    return _staircase(n, CACHE)


def test_function(test_case):
    answer = staircase(test_case[0])
    if answer == test_case[1]:
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    test_case = [4, 7]
    test_function(test_case)

    test_case = [5, 13]
    test_function(test_case)

    test_case = [3, 4]
    test_function(test_case)

    test_case = [20, 121415]
    test_function(test_case)