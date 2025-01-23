#Before your for loop, create a new variable named distances and assign it an empty dictionary.

def shortest_path(graph, start):
    unvisited = []
    distances = {}
    for node in graph:
        unvisited.append(node)