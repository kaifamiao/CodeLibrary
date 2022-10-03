def subsets(array: list) -> list:
    """
    Returns all the subsets of the given list.
    """
    if len(array) <= 1:
        return [array]
    else:
        subset_list = [array]
        for i in range(len(array)):
            subset_list.extend(subsets(array[:i] + array[i+1:]))
        
        subset_unique = []
        for i, elem in enumerate(subset_list):
            if i == subset_list.index(elem):
                subset_unique.append(elem)

        return subset_unique


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = subsets(arr)
        
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    arr = [9]
    solution = [[9]]
    test_case = [arr, solution]
    test_function(test_case)

    arr = [5, 7]
    solution = [[7], [5], [5, 7]]
    test_case = [arr, solution]
    test_function(test_case)

    arr = [9, 12, 15]
    solution = [[15], [12], [12, 15], [9], [9, 15], [9, 12], [9, 12, 15]]
    test_case = [arr, solution]
    test_function(test_case)

    arr = [9, 8, 9, 8]
    solution = [[8],
    [9],
    [9, 8],
    [8, 8],
    [8, 9],
    [8, 9, 8],
    [9, 9],
    [9, 9, 8],
    [9, 8, 8],
    [9, 8, 9],
    [9, 8, 9, 8]]
    test_case = [arr, solution]
    test_function(test_case)
