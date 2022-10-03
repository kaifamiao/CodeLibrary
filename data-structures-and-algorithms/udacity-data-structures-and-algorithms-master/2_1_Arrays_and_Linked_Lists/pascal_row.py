def nth_pascal_row(n: int) -> list:
    """
    Returns the nth row of the Pascal's triangle.
    
    Args:
        n (int): the row.
    Returns:
        list: entries of the nth row of the Pascal's triangle.
    """
    row = [1]
    for i in range (1, n + 1):
        row.append(int(row[i-1] * (n - i + 1) / (i)))
    return row


def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = nth_pascal_row(n)
    if solution == output:
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    n = 0
    solution = [1]
    test_case = [n, solution]
    test_function(test_case)

    n = 1
    solution = [1, 1]
    test_case = [n, solution]
    test_function(test_case)

    n = 2
    solution = [1, 2, 1]
    test_case = [n, solution]
    test_function(test_case)

    n = 3
    solution = [1, 3, 3, 1]
    test_case = [n, solution]
    test_function(test_case)

    n = 4
    solution = [1, 4, 6, 4, 1]
    test_case = [n, solution]
    test_function(test_case)