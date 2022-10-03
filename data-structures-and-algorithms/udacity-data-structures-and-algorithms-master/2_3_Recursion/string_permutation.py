def permute(string: str) -> list:
    """
    Returns all the permutations of the letters of the
    given string.
    """
    permuations = []
    if len(string) <= 1:
        permuations.append(string)
        return permuations
    
    for i, letter in enumerate(string):
        for permutation in permute(string[:i] + string[i+1:]):
            permuations += [letter + permutation]
    
    return permuations


def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = permute(string)
    
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")
    

if __name__ == '__main__':
    string = 'ab'
    solution = ['ab', 'ba']
    test_case = [string, solution]
    test_function(test_case)

    string = 'abc'
    output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
    test_case = [string, output]
    test_function(test_case)

    string = 'abcd'
    output = ['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb', 'cdab', 'cdba', 'abdc', 'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba']
    test_case = [string, output]
    test_function(test_case)

