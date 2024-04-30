#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, num1, num2):
        # code here
        # return head of sum list
        s1,s2='',''
        
        while num1:
            s1+=str(num1.data)
            num1=num1.next
        
        while num2:
            s2+=str(num2.data)
            num2=num2.next
        res=str(int(s1)+int(s2))
        
        a=b=Node(res[0])
        for i in res[1:]:
            a.next=Node(i)
            a=a.next
        return b
        
