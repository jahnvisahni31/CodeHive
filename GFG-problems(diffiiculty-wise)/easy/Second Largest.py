class Solution:
	def print2largest(self,arr, n):
		# code here
		m = float('-inf')
		s = float('-inf')
		for nu in arr:
		    if nu > m:
		        s = m
		        m = nu
		    elif nu < m and nu > s:
		        s = nu
		if s == float('-inf'):
		    return -1
		else:
		    return s
		    
