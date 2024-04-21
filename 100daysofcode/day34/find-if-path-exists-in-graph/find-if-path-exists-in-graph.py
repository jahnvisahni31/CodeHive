class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = {i: [] for i in range(n)}
        for edge in edges:
            u, v = edge
            adj_list[u].append(v)
            adj_list[v].append(u)  # Since it's a bidirectional graph, add both directions

        # Define the DFS function
        def dfs(node, destination, visited):
            if node == destination:
                return True
            visited[node] = True
            for neighbor in adj_list[node]:
                if not visited[neighbor]:
                    if dfs(neighbor, destination, visited):
                        return True
            return False

        # Initialize the visited array and start the DFS traversal
        visited = [False] * n
        return dfs(source, destination, visited)
        
