class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	u = set()
    	d = set()
    	for e in arr:
    	    if e in u:
    	        d.add(e)
    	    else:
    	        u.add(e)
    	if len(d) == 0:
    	    return [-1]
    	return sorted(list(d))
