class Solution:
    def kPalindrome(self, str, n, k):
        # code here
        def is_palindrome(s):
            return s == s[::-1]

        dp = [[0 for _ in range(n)] for _ in range(n)]

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if str[i] == str[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])

        return 1 if dp[0][n - 1] <= k else 0
