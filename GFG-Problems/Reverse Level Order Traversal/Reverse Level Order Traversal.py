'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def reverseLevelOrder(root):
    # code here
    if root is None:
       return
    queue = []
    stack = []
    result = []
   
    queue.append(root)
    while len(queue) > 0:
        node = queue.pop(0)
        stack.append(node)
       
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
   
    while len(stack) > 0:
        node = stack.pop()
        result.append(node.data)
   
    return result
