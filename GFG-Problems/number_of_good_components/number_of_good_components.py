from typing import List
from collections import defaultdict


class Solution:
    def findNumberOfGoodComponent(self, e : int, v : int, edges : List[List[int]]) -> int:
        # code here
        graph = defaultdict(list)
        for fro, to in edges:
            graph[fro].append(to)
            graph[to].append(fro)
            
        def dfs(vertex, nei):
            nonlocal flag, count
            vis.add(vertex)
            count += 1
            if len(graph[vertex]) != nei:
                flag = False
            for n in graph[vertex]:
                if n not in vis:
                    dfs(n, nei)
            flag = flag & True
        ans = 0
        vis = set()
        for i in range(1, v+1):
            # print(vis)
            nei = len(graph[i])
            count = -1
            flag = True
            if i not in vis:
                dfs(i, nei)
                # print(count)
                if flag and count == nei:
                    # print(i)
                    ans += 1
        return ans
