#User function Template for python3

"""
# Node Class

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    #Function to reverse a linked list.
    def arrangeCV(self, head):
        # Code here
        if head is None or head.next is None:
            return head 
        vowel_head = vowel_curr = Node(0) 
        consonant_head = consonant_curr = Node(0)
        curr = head

        while curr:
            if curr.data in ['a', 'e', 'i', 'o', 'u']:
                vowel_curr.next = curr
                vowel_curr = vowel_curr.next
            else:
                consonant_curr.next = curr
                consonant_curr = consonant_curr.next
            curr = curr.next
        vowel_curr.next = consonant_head.next
        consonant_curr.next = None 
        return vowel_head.next
