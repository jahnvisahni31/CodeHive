class Solution:
    def findSingle(self, n, arr):
        # code here
        result = 0

    # XOR all the integers in the array
        for num in arr:
            result ^= num

        return result


#Expected Time Complexity: O(n)
#Expected Auxiliary Space: O(1)
