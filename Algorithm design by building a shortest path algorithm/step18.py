#Add another node connected to B to your graph and call it C.

#Modify your existing dictionary to represent this arrangement: add another key 'C' to my_graph and give it the value of the string 'B'.

#Also, change the value of the existing 'B' key into the list ['A', 'C'] to represent the multiple connections of your 'B' node.

my_graph = {
    'A': 'B',
    'B': ['A', 'C'],
    'C': 'B'
}