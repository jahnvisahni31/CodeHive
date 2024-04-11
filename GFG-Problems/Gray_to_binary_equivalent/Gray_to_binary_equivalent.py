
class Solution:    
    ##Complete this function
    # function to convert a given Gray equivalent n to Binary equivalent.
    def grayToBinary(self,n):
        ##Your code here
        binary = 0
        while n:
            binary ^= n
            n >>= 1
        return binary
