#User function Template for python3
from queue import Queue


'''
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def KDistance(self,root,k):
        '''
        :param root: root of given tree.
        :param k: distance k from root
        :return: list of all nodes that are at distance k from root.
        '''
        # code here
        if root is None or k < 0:
            return []
        queue = [root]
        current_level = 0
        while queue:
            if current_level == k:
                return [node.data for node in queue]
            next_level = []
            for node in queue:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            queue = next_level
            current_level += 1
        return []
