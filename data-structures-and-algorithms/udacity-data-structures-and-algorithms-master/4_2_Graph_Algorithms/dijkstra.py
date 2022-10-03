import math

from weighted_graph import GraphEdge, GraphNode, Graph


def dijkstra(graph: Graph, start_node: GraphNode, end_node: GraphNode) -> int:
    """
    Finds and returns the shortest path from start_node to end_node.

    Args:
        start_node (GraphNode): starting node
        end_node (GraphNode): ending node
    Returns:
        int: shortest path from start_node to end_node
    """
    distances_not_visited = {node: math.inf for node in graph.nodes}
    distances_not_visited[start_node] = 0
    shortest_paths = {}

    while len(distances_not_visited) > 0:
        nearest_node, nearest_distance = sorted(distances_not_visited.items(), key=lambda x: x[1])[0]
        shortest_paths[nearest_node] = distances_not_visited.pop(nearest_node)
        
        for edge in nearest_node.edges:
            if edge.node in distances_not_visited:
                new_distance = nearest_distance + edge.distance
                if distances_not_visited[edge.node] > new_distance:
                    distances_not_visited[edge.node] = new_distance
    return shortest_paths[end_node]


if __name__ == '__main__':
    node_u = GraphNode('U')
    node_d = GraphNode('D')
    node_a = GraphNode('A')
    node_c = GraphNode('C')
    node_i = GraphNode('I')
    node_t = GraphNode('T')
    node_y = GraphNode('Y')

    graph = Graph([node_u, node_d, node_a, node_c, node_i, node_t, node_y])
    graph.add_edge(node_u, node_a, 4)
    graph.add_edge(node_u, node_c, 6)
    graph.add_edge(node_u, node_d, 3)
    graph.add_edge(node_d, node_u, 3)
    graph.add_edge(node_d, node_c, 4)
    graph.add_edge(node_a, node_u, 4)
    graph.add_edge(node_a, node_i, 7)
    graph.add_edge(node_c, node_d, 4)
    graph.add_edge(node_c, node_u, 6)
    graph.add_edge(node_c, node_i, 4)
    graph.add_edge(node_c, node_t, 5)
    graph.add_edge(node_i, node_a, 7)
    graph.add_edge(node_i, node_c, 4)
    graph.add_edge(node_i, node_y, 4)
    graph.add_edge(node_t, node_c, 5)
    graph.add_edge(node_t, node_y, 5)
    graph.add_edge(node_y, node_i, 4)
    graph.add_edge(node_y, node_t, 5)

    print('Shortest Distance from {} to {} is {}'.format(node_u.value, node_y.value, dijkstra(graph, node_u, node_y)))