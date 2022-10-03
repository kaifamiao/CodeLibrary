from collections import deque

from graph import GraphNode, Graph


def bfs_search(root: GraphNode, value: any) -> GraphNode:
    """
    Traverses graph in depth first order to search for the value.

    Args:
        root (GraphNode): root of the graph
        value (any): value to be searched
    Returns:
        GraphNode: node containing the value, -1 if not found
    """
    if root is None:
        return -1
    
    queue = deque()
    visited = {}

    node = root
    queue.append(node)
    visited[node] = True

    while len(queue) > 0:
        node = queue.popleft()
        if node.value == value:
            return node
        for child in node.children:
            if child not in visited:
                queue.append(child)
    return -1


if __name__ == '__main__':
    nodeG = GraphNode('G')
    nodeR = GraphNode('R')
    nodeA = GraphNode('A')
    nodeP = GraphNode('P')
    nodeH = GraphNode('H')
    nodeS = GraphNode('S')

    graph1 = Graph([nodeS,nodeH,nodeG,nodeP,nodeR,nodeA] ) 
    graph1.add_edge(nodeG,nodeR)
    graph1.add_edge(nodeA,nodeR)
    graph1.add_edge(nodeA,nodeG)
    graph1.add_edge(nodeR,nodeP)
    graph1.add_edge(nodeH,nodeG)
    graph1.add_edge(nodeH,nodeP)
    graph1.add_edge(nodeS,nodeR)
    
    assert nodeA == bfs_search(nodeS, 'A')
    assert nodeS == bfs_search(nodeP, 'S')
    assert nodeR == bfs_search(nodeH, 'R')
