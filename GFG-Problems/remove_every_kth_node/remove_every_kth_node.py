class node:
    def __init__(self,x):
        self.data = x
        self.next = None


class Solution:
    def deleteK(self, head, k):
        #code here  
        c = head
        pr = None
        co = 1
        while c:
            if co % k == 0:
                if pr:
                    pr.next = c.next
                else:
                    head = c.next
            else:
                pr = c
            co += 1
            c = c.next
        return head
            
            
