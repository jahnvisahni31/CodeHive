class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        le = [node for node in adj if len(adj[node])== 1]
        while n >2:
            n -= len(le)
            ne = []
            for u in le:
                v = adj[u].pop()
                adj[v].remove(u)
                if len(adj[v]) == 1:
                    ne.append(v)
            le = ne
        return le
        
