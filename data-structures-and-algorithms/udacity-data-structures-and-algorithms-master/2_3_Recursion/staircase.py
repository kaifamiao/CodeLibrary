def staircase(n: int) -> int:
    """
    Calculates how many ways one can climb n stairs by taking
    1, 2, or 3 steps.
    """
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        ways = 0
        ways += staircase(n - 1)
        ways += staircase(n - 2)
        ways += staircase(n - 3)
        return ways


def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = staircase(n)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    n = 3
    solution = 4
    test_case = [n, solution]
    test_function(test_case)

    n = 4
    solution = 7
    test_case = [n, solution]
    test_function(test_case)

    n = 7
    solution = 44
    test_case = [n, solution]
    test_function(test_case)
