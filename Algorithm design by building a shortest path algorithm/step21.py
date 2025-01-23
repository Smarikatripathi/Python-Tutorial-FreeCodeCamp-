#Now modify my_graph['B'] into a list of tuples, where the first element in the tuple is the connected node, and the second element is the distance. The B-C distance is 4.

my_graph = {
    'A': [('B', 3), ('D', 1)],
    'B': [('A', 3), ('C', 4)],
    'C': ['B', 'D'],
    'D': ['A', 'C']
}