#User function Template for python3

'''
class Node:
            def __init__(self, data):
                self.data = data
                self.left = self.right = None
'''

#Function to return a tree created from postorder and inoreder traversals.
class Solution:
    def buildTree(self,In, post, n):
        # your code here
        def build(In, post):
            if not In:
                return None
            root = Node(post[-1])
            i = In.index(post[-1])
            root.left = build(In[:i],post[:i])
            root.right = build(In[i+1:], post[i:len(post)-1])
            return root
        return build(In, post)
