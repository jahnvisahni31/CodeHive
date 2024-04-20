class Solution:
    #Function to partition the array around the range such 
    #that array is divided into three parts.
	def threeWayPartition(self, array, a, b):
	    # code here 
	    l, m, h = 0, 0, len(array) - 1
	    while m <= h:
	        if array[m] < a:
	            array[l], array[m] = array[m], array[l]
	            l += 1
	            m += 1
	        elif array[m] >= a and array[m] <= b:
	            m += 1
	        else:
	            array[m], array[h] = array[h], array[m]
	            h -= 1
	    
	    return 1
