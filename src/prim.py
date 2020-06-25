""" 
Connect Islands using Prim’s Algorithm
In an ocean, there are n islands some of which are connected via bridges. Travelling 
over a bridge has some cost attaced with it. Find bridges in such a way that all 
islands are connected with minimum cost of travelling.
You can assume that there is at least one possible way in which all islands are 
connected with each other.

You will be provided with two input parameters:
    1. num_islands = number of islands
    2. bridge_config = list of lists. Each inner list will have 3 elements:
      a. island A
      b. island B
      c. cost of bridge connecting both islands
Each island is represented using a number

Example:
    num_islands = 4
    bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]

Input parameters explanation:
1. Number of islands = 4
2. Island 1 and 2 are connected via a bridge with cost = 1
   Island 2 and 3 are connected via a bridge with cost = 4
   Island 1 and 4 are connected via a bridge with cost = 3
   Island 4 and 3 are connected via a bridge with cost = 2
   Island 1 and 3 are connected via a bridge with cost = 10

In this example if we are connecting bridges like this...
    between 1 and 2 with cost = 1
    between 1 and 4 with cost = 3
    between 4 and 3 with cost = 2
...then we connect all 4 islands with cost = 6 which is the minimum traveling cost.
"""
from Graph import Graph, GraphNode, GraphEdge
import heapq

""" 
Prim's Minimum Spanning Tree algorithm
Find the minimum cost required to travel all islands via bridges
:param: bridge_config - bridge configuration as explained in the problem statement
return: cost (int) minimum cost of connecting all islands
"""
def create_graph(bridge_config):
    nodes_set = set(node for t in bridge_config for node in t[0:2])
    max_node = max(nodes_set)
    graph = [list() for _ in range(max_node + 1)]
    # create undirected graph as an adjacency list
    for source, target, cost in bridge_config:
        graph[source].append((target, cost))
        graph[target].append((source, cost))
    return graph

def prim(graph):
    # create blank min_heap and push any graph node into it
    # heap is represented as a list of (cost, neighbour) tuples
    # (first element of tuple determines the order of elements in the heap)
    start_node = 1
    min_heap = [(0, start_node)]
    total_cost = 0
    visited = []
    while len(min_heap) > 0:
        edge_cost, current_node = heapq.heappop(min_heap)
        if current_node in visited:
            continue

        total_cost += edge_cost
        for neighbour, edge_cost in graph[current_node]:
            heapq.heappush(min_heap, (edge_cost, neighbour))
        visited.append(current_node)
    return total_cost

def get_minimum_cost_of_connecting(bridge_config):
    graph = create_graph(bridge_config)
    return prim(graph)

def test_function(test_case):
    num_islands = test_case[0]
    bridge_config = test_case[1]
    solution = test_case[2]
    output = get_minimum_cost_of_connecting(bridge_config)
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")

# Test case 1
num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
solution = 6

test_case = [num_islands, bridge_config, solution]
test_function(test_case)

# Test case 2
num_islands = 5
bridge_config = [[1, 2, 5], [1, 3, 8], [2, 3, 9]]
solution = 13

test_case = [num_islands, bridge_config, solution]
test_function(test_case)

# Test case 3
num_islands = 5
bridge_config = [[1, 2, 3], [1, 5, 9], [2, 3, 10], [4, 3, 9]]
solution = 31

test_case = [num_islands, bridge_config, solution]
test_function(test_case)
