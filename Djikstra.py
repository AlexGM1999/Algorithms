
from collections import defaultdict

class Graph():
    def __init__(self):
   
        self.edges = defaultdict(list)
        self.weights = {}
    
    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight

graph = Graph()

edges = [
    ('1', '2', 7),
    ('1', '3', 1),
    ('1', '5', 3),
    ('2', '5', 9),
    ('2', '4', 2),
    ('2', '8', 5),
    ('3', '5', 5),
    ('3', '6', 4),
    ('4', '7', 4),
    ('4', '8', 7),
    ('5', '8', 8),
    ('5', '9', 6),
    ('5', '10', 5),
    ('6', '9', 2),
    ('7', '11', 3),
    ('8', '10', 4),
    ('8', '11', 2),
    ('9', '10', 8),
    ('10', '11', 7),
]

for edge in edges:
    graph.add_edge(*edge)

def dijsktra(graph, initial, end):

    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)              
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
                    
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
   
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
 
    path = path[::-1]
    print("Fmin=" ,weight)
    return path

print(dijsktra(graph, '1', '11'))
