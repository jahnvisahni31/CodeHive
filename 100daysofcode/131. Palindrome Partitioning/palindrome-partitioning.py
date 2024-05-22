class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for l in range(n):
            for i in range(n - l):
                j = i + l
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
        def dfs(start, path, result):
            if start == n:
                result.append(path[:])  # Valid partition found
                return
            for end in range(start, n):
                if dp[start][end]:  # Check if substring is a palindrome
                    path.append(s[start:end+1])
                    dfs(end + 1, path, result)  # Recurse to next position
                    path.pop()  # Backtrack
        
        result = []
        dfs(0, [], result)  # Start DFS search
        return result
