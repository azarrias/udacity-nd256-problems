from Graph import Graph, GraphEdge, GraphNode
from operator import itemgetter
from collections import defaultdict
import heapq

"""
Create directed graph represented as an adjacency list
"""
def create_graph(edges):
    graph = defaultdict(list)
    for source, target, cost in edges:
        graph[source].append((target, cost))
    return graph

"""
Find the shortest path from the source node to the target node in the given graph.
Note - This improved implementation of the Dijkstra's algorithm has a O(nlogn) time
complexity, since it uses an adjacency list and a min_heap.
Dijkstra's algorithm does not work if the are edges with negative weights.
"""
def dijkstra(graph, start_node, end_node):
    min_heap = [(0, start_node)]
    costs = {start_node: 0}
    visited = set()
    # store the smallest cost to each node of the graph, from the starting node
    result = {}

    while len(min_heap) > 0:
        # pick the node with the lowest cost
        current_node_cost, current_node = heapq.heappop(min_heap)
        if current_node in visited:
            continue
        # remove that lowest cost node from the costs dictionary and store it in the result dictionary
        result[current_node] = current_node_cost

        # for each neighbour of current_node, if the cost is smaller than the one stored, update it
        for neighbour, edge_cost in graph[current_node]:
            if neighbour in visited:
                continue
            cost_to_target = current_node_cost + edge_cost
            if costs.get(neighbour, None) is None or cost_to_target < costs[neighbour]:
                costs[neighbour] = cost_to_target
                heapq.heappush(min_heap, (cost_to_target, neighbour))
    
    return result[end_node]

# Test Case 1:
# Create a graph
edges = [["U", "A", 4], ["U", "C", 6], ["U", "D", 3], ["D", "C", 4], ["A", "I", 7], ["C", "I", 4], ["C", "T", 5], ["I", "Y", 4], ["T", "Y", 5]]
graph = create_graph(edges)
# Shortest Distance from U to Y is 14
print('Shortest Distance from {} to {} is {}'.format("U", "Y", dijkstra(graph, "U", "Y")))

# Test Case 2
edges = [["A", "B", 5], ["B", "C", 5], ["A", "C", 10]]
graph = create_graph(edges)
# Shortest Distance from A to C is 10
print('Shortest Distance from {} to {} is {}'.format("A", "C", dijkstra(graph, "A", "C")))

# Test Case 3
edges = [["A", "B", 3], ["A", "D", 2], ["B", "D", 4], ["B", "E", 6], ["B", "C", 1], ["C", "E", 2], ["E", "D", 1]]
graph = create_graph(edges)
# Shortest Distance from A to C is 4
print('Shortest Distance from {} to {} is {}'.format("A", "C", dijkstra(graph, "A", "C")))