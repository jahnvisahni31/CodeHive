class Solution:
    def printKClosest(self, arr, n, k, x):
        # code here
        heap = []
        
        for val in arr[::-1] :
            if val==x:
                continue
            dist = abs(val - x)
            
            if len(heap) < k:
                heappush(heap, (-1 * dist, val))
            else:
                if -1 * heap[0][0] > dist:
                    heappop(heap)
                    heappush(heap, (-1 * dist, val))
                    
        result = []
        while heap:
            _, val = heappop(heap)
            result.append(val)
        return result[::-1]
