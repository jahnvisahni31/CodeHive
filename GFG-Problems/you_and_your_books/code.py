class Solution:
    #Your task is to complete this function
    #Function should return an integer
    #a - list/array containing height of stack's respectively
    def max_Books(self, n, k, arr):
        #code here
        n = len(arr)
        start = 0
        curr_sum = 0
        max_books = 0
        for i in range(n):
            if arr[i]<=k:
                curr_sum +=arr[i]
                max_books = max(max_books, curr_sum)
            else:
                curr_sum = 0
                start = i + 1

        return max_books
