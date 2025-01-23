#After appending node to unvisited in your loop, create an if statement that triggers if the node is equal to the starting node. Then assign 0 to that node inside the distances dictionary.
def shortest_path(graph, start):
    unvisited = []
    distances = {}
    for node in graph:
        unvisited.append(node)
        if node == start:
            distances[node] = 0