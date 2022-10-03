def lcs(string_a: str, string_b: str) -> int:
    """
    Returns the length of the longest common subsequence of the given strings.

    Args:
        string_a (str): first string
        string_b (str): another string
    Returns
        int: the length of the longest common sequence
    """
    len_a = len(string_a)
    len_b = len(string_b)

    memo = [[None] * (len_b+1) for _ in range(len_a+1)]

    for i in range(len_a + 1):
        for j in range(len_b + 1):
            if i == 0 or  j == 0:
                memo[i][j] = 0
            elif string_a[i-1] == string_b[j-1]:
                memo[i][j] = memo[i-1][j-1] + 1
            else:
                memo[i][j] = max(memo[i-1][j], memo[i][j-1])
    return memo[len_a][len_b]


if __name__ == '__main__':
    test_A1 = "WHOWEEKLY"
    test_B1 = "HOWONLY"
    lcs_val1 = lcs(test_A1, test_B1)
    test_A2 = "CATSINSPACETWO"
    test_B2 = "DOGSPACEWHO"
    lcs_val2 = lcs(test_A2, test_B2)

    print('LCS val 1 = ', lcs_val1)
    assert lcs_val1==5, "Incorrect LCS value."
    print('LCS val 2 = ', lcs_val2)
    assert lcs_val2==7, "Incorrect LCS value."
    print('Tests passed!')