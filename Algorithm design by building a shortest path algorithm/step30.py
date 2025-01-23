#After your for loop, add a print() call and pass in the following string to see the values of the variables you have created: f'Unvisited: {unvisited}\nDistances: {distances}'.

def shortest_path(graph, start):
    unvisited = []
    distances = {}
    for node in graph:
        unvisited.append(node)
        if node == start:
            distances[node] = 0
        else:
            distances[node] = float('inf')
    print(f'Unvisited: {unvisited}\nDistances: {distances}')