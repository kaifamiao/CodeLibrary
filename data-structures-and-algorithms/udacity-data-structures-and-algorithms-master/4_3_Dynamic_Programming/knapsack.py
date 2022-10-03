from collections import namedtuple


Item = namedtuple('Item', ['weight', 'value'])


def knapsack(max_weight: int, items: list, n: int, memo: list) -> int:
    if max_weight <= 0 or n < 0:
        return 0
    elif memo[n][max_weight] is not None:
        return memo[n][max_weight]
    elif items[n].weight > max_weight:
        result = knapsack(max_weight, items, n-1, memo)
    else:
        temp1 = knapsack(max_weight, items, n-1, memo)
        temp2 = items[n].value + knapsack(max_weight-items[n].weight, items, n-1, memo)
        result = max(temp1, temp2)
    memo[n][max_weight] = result
    return result


def max_value(max_weight: int, items: list) -> int:
    """
    Returns the maximum value of the knapsack given the weight constraints.

    Args:
        max_weight (int): maximum weight
        items (list): list of weights and values
    Returns:
        int: maximum value
    """
    memo = [[None for _ in range(max_weight+1)] for _ in range(len(items))]
    items = sorted(items, key=lambda x: x.weight)
    knapsack(max_weight, items, len(items)-1, memo)
    result = memo[len(items)-1][max_weight]
    return result


if __name__ == '__main__':
    tests = [
        {
            'correct_output': 14,
            'input':
                {
                    'max_weight': 15,
                    'items': [Item(10, 7), Item(9, 8), Item(5, 6)]}},
        {
            'correct_output': 13,
            'input':
                {
                    'max_weight': 25,
                    'items': [Item(10, 2), Item(29, 10), Item(5, 7), Item(5, 3), Item(5, 1), Item(24, 12)]}}]

    for test in tests:
        assert test['correct_output'] == max_value(**test['input'])
