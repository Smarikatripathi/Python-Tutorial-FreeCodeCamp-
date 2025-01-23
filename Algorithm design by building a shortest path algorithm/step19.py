#Add one last node, 'D', which is connected with 'A' and 'C'.

#Modify your dictionary to represent this structure. Again, use a list to represent multiple connections.


my_graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['A', 'C']
}
