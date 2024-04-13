class Solution:
    def reversedBits(self, x):
        # code here 
        binary_x = format(x, '032b')  # Convert x to a 32-bit binary representation
        reversed_binary_x = binary_x[::-1]  # Reverse the binary representation
        decimal_result = int(reversed_binary_x, 2)  # Convert the reversed binary back to decimal
        return decimal_result
