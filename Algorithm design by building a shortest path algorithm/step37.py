#Add \nPaths: {paths} at the end of the f-string passed to the print call, so that it prints the paths variable, too.
def shortest_path(graph, start):
    unvisited = list(graph)
    distances = {node: 0 if node == start else float('inf') for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)
    
    print(f'Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}')
    
shortest_path(my_graph, 'A')