#After the distances variable, create a paths variable and assign it a dictionary with all the keys from graph. Assign an empty list to each key and use a dictionary comprehension to build your dictionary.

def shortest_path(graph, start):
    unvisited = list(graph)
    distances = {}
    paths = {node: [] for node in graph}
    
    print(f'Unvisited: {unvisited}\nDistances: {distances}')
    
shortest_path(my_graph, 'A')