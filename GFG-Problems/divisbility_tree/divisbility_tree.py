
from typing import List
from collections import defaultdict


class Solution:
    def minimumEdgeRemove(self, n : int, edges : List[List[int]]) -> int:
        # code here
        counts = [0]*(n+1)
        graph = [[] for _ in range(n+1)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node,prev,counts,graph):
            size = 1
            for neigh in graph[node]:
                if neigh == prev:
                    continue
                size += dfs(neigh,node,counts,graph)
            
            counts[node] = size
            return size
        
        dfs(1,-1,counts,graph)
        ans = 0
        for i in range(2,n+1):
            if counts[i] % 2 == 0:
                ans += 1
                
        return ans
