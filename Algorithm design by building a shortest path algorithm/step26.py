#Create a for loop to iterate over your graph, and use the .append() method to add each node to the end of the unvisited list.

def shortest_path(graph, start):
    unvisited = []
    for i in graph:
        unvisited.append(i)