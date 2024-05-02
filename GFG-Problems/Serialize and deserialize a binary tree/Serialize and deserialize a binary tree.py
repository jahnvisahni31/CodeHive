#User function Template for python3


'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to serialize a tree and return a list containing nodes of tree.
    def serialize(self, root):
        #code here
        def encode(node, arr):
            if node is not None:
                arr.append(node.data)
                encode(node.left, arr)
                encode(node.right, arr)
            else:
                arr.append('#')  # Use '#' to represent null nodes
    
        serialized_array = []
        encode(root, serialized_array)
        return serialized_array
    
    #Function to deserialize a list and construct the tree.   
    def deSerialize(self, a):
        #code here
        def decode(arr):
            val = arr.pop(0)
            if val == '#':
                return None
            node = Node(int(val))
            node.left = decode(arr)
            node.right = decode(arr)
            return node
    
        return decode(a)
