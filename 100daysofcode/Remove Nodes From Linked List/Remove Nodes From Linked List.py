# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        def re(node):
            pr, cu = None, node
            while cu:
                te = cu.next
                cu.next = pr
                pr = cu
                cu = te
            return pr
        r = re(head)
        ma = float("-inf")
        du = ListNode(0)
        du.next = r
        pr = du
        cu = r
        while cu:
            if cu.val >= ma:
                ma = cu.val
                pr = cu
                cu = cu.next
            else:
                pr.next = cu.next
                cu = cu.next

        m = re(du.next)
        return m
        
