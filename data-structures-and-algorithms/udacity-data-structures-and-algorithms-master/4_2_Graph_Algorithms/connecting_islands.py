import heapq


def adjacent_graph(num_islands: int, bridge_config: list) -> list:
    """
    Transforms a bridge configuration into an adjacency list.

    Args:
        num_islands (int): number of islands
        bridge_config (list[list]): bridge connection configuration list
    Returns:
        list: adjacency list of bridge confihuration
    """
    adjacency_list = [[] for _ in range(num_islands+1)]

    for bridge in bridge_config:
        adjacency_list[bridge[0]].append((bridge[1], bridge[2]))
        adjacency_list[bridge[1]].append((bridge[0], bridge[2]))

    return adjacency_list


def min_connections(graph: list) -> int:
    """
    """
    visited = [False for _ in range(len(graph)+1)]
    cost = 0

    heap = []
    heapq.heappush(heap, (0, 1))

    while len(heap) > 0:
        minimum_cost, island = heapq.heappop(heap)
        if not visited[island]:
            visited[island] = True
            cost += minimum_cost
            for nearby_island, nearby_cost in graph[island]:
                if not visited[nearby_island]:
                    heapq.heappush(heap, (nearby_cost, nearby_island))
    return cost


def test_function(test_case):
    num_islands = test_case[0]
    bridge_config = test_case[1]
    solution = test_case[2]
    output = min_connections(adjacent_graph(num_islands, bridge_config))
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    num_islands = 4
    bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
    solution = 6
    test_case = [num_islands, bridge_config, solution]
    test_function(test_case)

    num_islands = 5
    bridge_config = [[1, 2, 5], [1, 3, 8], [2, 3, 9]]
    solution = 13
    test_case = [num_islands, bridge_config, solution]
    test_function(test_case)

    num_islands = 5
    bridge_config = [[1, 2, 3], [1, 5, 9], [2, 3, 10], [4, 3, 9]]
    solution = 31
    test_case = [num_islands, bridge_config, solution]
    test_function(test_case)
