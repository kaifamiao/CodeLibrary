import copy

def permute(l: list) -> list:
    """Returns all the permutations of the given list."""
    permutations = []
    
    if len(l) <= 1:
        permutations.append(l)
        return permutations
    
    for i, elem in enumerate(l):
        for permutation in permute(l[:i] + l[i+1:]):
            permutations.append([elem] + permutation)
    
    return permutations


def check_output(output, expected_output):
    o = copy.deepcopy(output)  # so that we don't mutate input
    e = copy.deepcopy(expected_output)  # so that we don't mutate input
    
    o.sort()
    e.sort()
    return o == e


if __name__ == '__main__':
    print ("Pass" if  (check_output(permute([]), [[]])) else "Fail")
    print ("Pass" if  (check_output(permute([0]), [[0]])) else "Fail")
    print ("Pass" if  (check_output(permute([0, 1]), [[0, 1], [1, 0]])) else "Fail")
    print ("Pass" if  (check_output(permute([0, 1, 2]), [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]])) else "Fail")