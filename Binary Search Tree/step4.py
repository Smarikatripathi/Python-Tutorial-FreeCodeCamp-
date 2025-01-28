#Inside the __init__ method, delete pass and assign the value of the key parameter to the key attribute of the node using self.key.

#This means that the key attribute of the TreeNode instance will be set to the value passed during the object's creation.
class TreeNode:
    def __init__(self, key):
        self.key = key