class Solution: 
    def countPairs(self,arr, n): 
        # Your code goes here
        if n <= 2:
            return 0
        res = []
        mp = {}
        count = 0
        for i in range(n):
            res.append(i * arr[i])
        dup = res[:]
        dup.sort()

        for i in range(n):
            index = dup.index(res[i])
            if res[i] == 0:
                dup.pop(index)
                continue
            dup.pop(index)
            count += index
        return count
