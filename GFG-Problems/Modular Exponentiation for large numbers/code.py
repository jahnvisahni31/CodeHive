#User function Template for python3

class Solution:
	def PowMod(self, x, n, m):
		# Code here
		result = 1
        while n > 0:
            if n % 2 == 1:
                result = (result * x) % m
            x = (x * x) % m
            n = n // 2
        return result
