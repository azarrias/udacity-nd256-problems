from Graph import Graph, GraphNode
from collections import deque

# Iterative version of Breadth First Search using a queue
def bfs_iterative(start_node, search_label):
    visited = set()
    queue = deque()
    queue.append(start_node)

    while len(queue) > 0:
        current_node = queue.popleft() #dequeue
        visited.add(current_node)
        if current_node.label == search_label:
            return current_node

        for edge in current_node.edges:
            if edge.target_node not in visited:
                queue.append(edge.target_node) #enqueue
    
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

    assert nodeA == bfs_iterative(nodeS, 'A')
    assert nodeS == bfs_iterative(nodeP, 'S')
    assert nodeR == bfs_iterative(nodeH, 'R')

