class Solution:
    def minSteps(self, d):
        # code here
        target = abs(d)  # Convert the destination to its absolute value
        
        steps = 0
        total = 0
        
        # Loop to calculate the minimum number of steps
        while total < target or (total - target) % 2 != 0:
            steps += 1
            total += steps
        
        return steps
