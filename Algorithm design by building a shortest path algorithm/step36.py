#Use the .append() method to append start to the paths[start] list.

def shortest_path(graph, start):
    unvisited = list(graph)
    distances = {node: 0 if node == start else float('inf') for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)
    
    print(f'Unvisited: {unvisited}\nDistances: {distances}')
    
shortest_path(my_graph, 'A')