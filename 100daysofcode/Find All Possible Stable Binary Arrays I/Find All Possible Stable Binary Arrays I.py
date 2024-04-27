class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        M = 10**9 + 7
        a = [[[0] * 2 for _ in range(zero + 1)] for _ in range(one + 1)]
        a[0][0][0] = a[0][0][1] = 1
        for m in range(one + 1):
            for n in range(zero + 1):
                for o in range(1, limit + 1):
                    if m - o >= 0:
                        a[m][n][1] = (a[m][n][1] + a[m - o][n][0]) % M
                    if n - o >= 0:
                        a[m][n][0] = (a[m][n][0] + a[m][n - o][1]) % M
        return (a[one][zero][0] + a[one][zero][1]) % M
