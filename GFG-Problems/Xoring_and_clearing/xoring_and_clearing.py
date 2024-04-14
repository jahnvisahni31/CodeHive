class Solution:
    def printArr(self, n, arr):
        # printing array elements with spaces
        for i in arr:
            print(i, end=" ")
        print()
        

    def setToZero(self, n, arr):
        # setting all elements to zero
        arr[:] = [0]*n
        

    def xor1ToN(self, n, arr):
        # doing xor with indices
        l = []
        for i in range(len(arr)):
            re = arr[i] ^ i
            l.append(re)
        arr[:] = l
            
