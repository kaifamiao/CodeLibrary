from graph import GraphNode, Graph


def _dfs_recursion(root: GraphNode, visited: dict) -> None:
    if root is None:
        return
    
    visited[root] = True
    print(root.value)
    
    for child in root.children:
        if child not in visited:
            _dfs_recursion(child, visited)
    

def dfs_recursion(root: GraphNode) -> None:
    """
    Recursively traverses the graph in depth first order and prints the values.

    Args:
        root (GraphNode): root of the graph
    Returns:
        None
    """
    visited = {}
    return _dfs_recursion(root, visited)


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

    dfs_recursion(nodeG)