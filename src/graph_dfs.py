from Graph import Graph, GraphNode
from collections import deque

def dfs_search(start_node, search_value):
    visited = set()
    stack = deque()
    stack.append(start_node)

    while len(stack) > 0:
        current_node = stack.pop()
        visited.add(current_node)
        if current_node.value == search_value:
            return current_node

        for neighbour in current_node.neighbours:
            if neighbour not in visited:
                stack.append(neighbour)
    
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
