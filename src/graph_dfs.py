from Graph import Graph, GraphNode
from collections import deque

# Iterative version of Depth First Search using a stack
def dfs_iterative(start_node, search_label):
    visited = set()
    stack = deque()
    stack.append(start_node)

    while len(stack) > 0:
        current_node = stack.pop()
        visited.add(current_node)
        if current_node.label == search_label:
            return current_node

        for edge in current_node.edges:
            if edge.target_node not in visited:
                stack.append(edge.target_node)

# Recursive version without the necessity of a stack
def dfs_recursive(start_node, search_label):
    visited = set()
    return dfs_recursive_helper(start_node, visited, search_label)

def dfs_recursive_helper(node, visited, search_label):
    if node.label == search_label:
        return node

    result = None
    visited.add(node)
    for edge in node.edges:
        if edge.target_node not in visited:
            result = dfs_recursive_helper(edge.target_node, visited, search_label)
            if result:
                break
    return result
    
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

    assert nodeA == dfs_iterative(nodeS, 'A')
    assert nodeS == dfs_iterative(nodeP, 'S')
    assert nodeR == dfs_iterative(nodeH, 'R')

    assert nodeA == dfs_recursive(nodeG, 'A')
    assert nodeA == dfs_recursive(nodeS, 'A')
    assert nodeS == dfs_recursive(nodeP, 'S')
    assert nodeR == dfs_recursive(nodeH, 'R')