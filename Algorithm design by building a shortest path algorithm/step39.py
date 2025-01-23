#Before the print call, create a while loop that runs while unvisited is not empty. Use the pass keyword to fill the loop body.

def shortest_path(graph, start):
    unvisited = list(graph)
    distances = {node: 0 if node == start else float('inf') for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)
    while unvisited:
        pass
    print(f'Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}')
    
#shortest_path(my_graph, 'A')