#Pass key=distances.get as the second argument to your min() call. In this way, the comparison will take place depending on the value each unvisited list item has inside the distances dictionary.

    while unvisited:
        current = min(unvisited, key=distances.get)