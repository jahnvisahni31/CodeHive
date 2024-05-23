class Solution:
    def missingNumber(self,array,n):
        # code here
        expected_sum = (n * (n + 1)) // 2
        actual_sum = sum(array)
        missing_element = expected_sum - actual_sum
        return missing_element



# Company Tags
# Flipkart Morgan Stanley Accolite Amazon Microsoft D-E-Shaw Ola Cabs 
