#Create an else clause and assign an infinite value to the node in the distances dictionary. For that, use the float() function with the string 'inf' as argument to generate a floating point number representing the positive infinity.

def shortest_path(graph, start):
    unvisited = []
    distances = {}
    for node in graph:
        unvisited.append(node)
        if node == start:
            distances[node] = 0
        else:
            distances[node] = float('inf')