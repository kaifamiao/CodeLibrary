from graph import GraphNode, Graph


def dfs_search(root: GraphNode, value: any) -> GraphNode:
    """
    Traverses graph in depth first order to search for the value.

    Args:
        root (GraphNode): root of the graph
        value (any): value to be searched
    Returns:
        GraphNode: node containing the value, -1 if not found
    """
    if root.value == value:
        return root
    
    stack = list()
    visited = list()
    node = root
    
    stack.append(node)
    visited.append(node)

    while len(stack) > 0:
        child_found = False
        for child in node.children:
            if child not in visited:
                if child.value == value:
                    return child
                node = child
                visited.append(node)
                stack.append(child)
                child_found = True
                break
        if not child_found:
            stack.pop()
            if len(stack) != 0:
                node = stack.pop()


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
    
    assert nodeA == dfs_search(nodeS, 'A')
    assert nodeS == dfs_search(nodeP, 'S')
    assert nodeR == dfs_search(nodeH, 'R')
