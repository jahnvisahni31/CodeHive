#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def deleteMid(self,head):
        '''
        head:  head of given linkedList
        return: head of resultant llist
        '''
        
        #code here
        if not head or not head.next:
            return None  # If the list is empty or has only one node, return None
        
        slow_pointer = head
        fast_pointer = head
        prev_node = None
        
        while fast_pointer and fast_pointer.next:
            prev_node = slow_pointer
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        
        # Skip the middle node
        prev_node.next = slow_pointer.next
        
        return head
    
