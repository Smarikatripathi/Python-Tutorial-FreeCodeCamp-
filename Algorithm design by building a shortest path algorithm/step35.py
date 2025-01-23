#Use a dictionary comprehension to create a dictionary based on graph and assign it to the distances variable. Give the key a value of zero if the node is equal to the starting node, and infinite otherwise. Use float('inf') to achieve the latter.

def shortest_path(graph, start):
    unvisited = list(graph)
    distances = {node: 0 if node == start else float('inf') for node in graph}
    paths = {node: [] for node in graph}
    print(f'Unvisited: {unvisited}\nDistances: {distances}')
    
shortest_path(my_graph, 'A')