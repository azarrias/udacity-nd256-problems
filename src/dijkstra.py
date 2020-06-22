from Graph import Graph

"""
Find the shortest path from the source node to every other node in the given graph.
Note - This implementation of the Dijkstra's algorithm is not very efficient. 
Currently it has a O(n^2) time complexity. We will see a better version in the next 
lesson - "Graph Algorithms" with O(nlogn) time complexity.
"""
def dijkstra(graph, source):
    # Declare and initialize result, unvisited, and path
    result = {key: float("Inf") for key in graph.nodes}
    result[source] = 0
    unvisited = set(graph.nodes)
    path = {}
    # As long as unvisited is non-empty
    while unvisited: 
        # 1. Find the unvisited node having smallest known distance from the source node.
        current_node = min(unvisited, key=result.__getitem__)
        # 2. For the current node, find all the unvisited neighbours. For this, you have calculate the distance of each unvisited neighbour.
        for neighbour_node in graph.neighbours[current_node]:
            cost = result[current_node] + graph.distances[(current_node, neighbour_node)]
        # 3. If the calculated distance of the unvisited neighbour is less than the already known distance in result dictionary, update the shortest distance in the result dictionary.        
            if cost < result[neighbour_node]:
                result[neighbour_node] = cost
        # 4. If there is an update in the result dictionary, you need to update the path dictionary as well for the same key.
                path[neighbour_node] = current_node
        # 5. Remove the current node from the unvisited set.
        unvisited.remove(current_node)
    return result

if __name__ == '__main__':
    testGraph = Graph()
    for node in ['A', 'B', 'C', 'D', 'E']:
        testGraph.add_node(node)

        testGraph.add_edge('A','B',3)
        testGraph.add_edge('A','D',2)
        testGraph.add_edge('B','D',4)
        testGraph.add_edge('B','E',6)
        testGraph.add_edge('B','C',1)
        testGraph.add_edge('C','E',2)
        testGraph.add_edge('E','D',1)

    print(dijkstra(testGraph, 'A'))     # {'A': 0, 'D': 2, 'B': 3, 'E': 3, 'C': 4}
