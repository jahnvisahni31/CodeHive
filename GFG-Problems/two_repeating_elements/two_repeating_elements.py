class Solution:
    
    #Function to find two repeated elements.
    def twoRepeated(self, arr , n):
        #Your code here
        freq = [0] * (n + 1)
        repeatingNumbers = []

        for num in arr:
            if freq[num] == 0:
                freq[num] = 1
            else:
                repeatingNumbers.append(num)

        return repeatingNumbers
