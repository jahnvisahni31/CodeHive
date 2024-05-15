class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue, safeness = deque(), [[-1] * n for _ in range(n)]
        unseen = set(product(range(n), range(n)))
        nei = lambda x,y: set(((x-1,y), (x,y-1), (x+1,y), (x,y+1))) & unseen
        
        for i, j in product(range(n),range(n)):
            if grid[i][j] == 1:
                safeness[i][j] = 0
                queue.append((0, i,j))
        
        while queue:
            
            s, x,y = queue.popleft()

            for X, Y in nei(x,y):
                if safeness[X][Y] == -1:
                    safeness[X][Y] = s + 1
                    queue.append((s+1, X,Y))

        heap = [(-safeness[-1][-1], n-1,n-1)]
        
        while heap:
            s ,x,y = heappop(heap)
            if (x,y) == (0,0): return min(-s,safeness[0][0])
            unseen.discard((x,y))

            for X, Y in nei(x,y):
                safe = max(s,-safeness[X][Y])
                heappush(heap,(safe, X,Y) )
                unseen.discard((X,Y))
            
        return -1
