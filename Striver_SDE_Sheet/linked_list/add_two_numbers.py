# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        re = ListNode(0)
        cu = re
        ca = 0
        while l1 or l2 or ca:
            va1 = l1.val if l1 else 0
            va2 = l2.val if l2 else 0
            s = va1 + va2 + ca
            ca, di = divmod(s, 10)
            cu.next = ListNode(di)
            cu = cu.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return re.next

        

# time complexity = 98.18%
#space complexity = 93.18%

# Step 1: Initialize Variables and Result Linked List
# We start by initializing the result linked list with a dummy head node and keeping a reference to the current node.

# Step 2: Add Digits Iteratively
# We then iterate through both input linked lists l1 and l2 simultaneously, adding the digits along with any carry from the previous operation.

# Step 3: Handle Carry and Digit Calculation
# Inside the iteration, we calculate the sum of the current digits of l1 and l2 along with the carry. We update the carry and calculate the digit to be added to the result linked list node.

# Step 4: Construct Result Linked List
# We construct the result linked list by appending a new node with the calculated digit to the result linked list.

# Step 5: Iterate to Next Nodes
# We move to the next nodes in l1 and l2 if they exist, and repeat the addition process.

# Step 6: Return the Result
