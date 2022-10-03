def lps(string: str) -> int:
    """
    Returns the length of longest palindromic subsequence in the given string.
    BEEKBEED
    Args:
        string (str): string
    Returns:
        int: lenght of the longest palindromic subsequence
    """
    n = len(string)
    memo = [[0] * n for _ in range(n)]

    # every subsequence of length 1 is a palindrome of length 1
    for i in range(n):
        memo[i][i] = 1
    
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i + l - 1
            if string[i] == string[j]:
                if l == 2:
                    memo[i][j] = 2
                else:
                    memo[i][j] = memo[i][j-1] + 2
            else:
                memo[i][j] = max(memo[i+1][j], memo[i][j-1])
    return memo[0][n-1]


def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = lps(string)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    string = "TACOCAT"
    solution = 7
    test_case = [string, solution]
    test_function(test_case)

    string = 'BANANA'
    solution = 5
    test_case = [string, solution]
    test_function(test_case)

    string = 'BANANO'
    solution = 3
    test_case = [string, solution]
    test_function(test_case)