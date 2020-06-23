from collections import defaultdict

class GraphNode(object):
    def __init__(self, label):
        self.label = label
        self.edges = []
        
    def add_neighbour(self, node, cost=None):
        self.edges.append(GraphEdge(node, cost))
    
    def remove_neighbour(self, node):
        for edge in self.edges:
            if edge.target_node == node:
                self.edges.remove(edge)

class GraphEdge(object):
    def __init__(self, target_node, cost):
        self.target_node = target_node
        self.cost = cost

class Graph(object):
    def __init__(self,node_list):
        self.nodes = node_list
        
    def add_edge(self, node1, node2, cost = None):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.add_neighbour(node2, cost)
            node2.add_neighbour(node1, cost)
            
    def remove_edge(self, node1, node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.remove_neighbour(node2)
            node2.remove_neighbour(node1)

class SimpleGraph:
    def __init__(self):
        self.nodes = set()                   # A set cannot contain duplicate nodes
        self.neighbours = defaultdict(list)  # Defaultdict is a child class of Dictionary that provides a default value for a key that does not exists.
        self.distances = {}                  # Dictionary. An example record as ('A', 'B'): 6 shows the distance between 'A' to 'B' is 6 units

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.neighbours[from_node].append(to_node)
        self.neighbours[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance    # lets make the graph undirected / bidirectional 
        
    def print_graph(self):
        print("Set of Nodes are: ", self.nodes)
        print("Neighbours are: ", self.neighbours)
        print("Distances are: ", self.distances)
