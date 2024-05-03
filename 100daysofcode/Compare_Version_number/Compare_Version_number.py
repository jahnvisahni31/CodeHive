class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        n1, n2 = len(v1), len(v2)
        ma = max(n1,n2)
        for i in range(ma):
            nu1 = v1[i] if i<n1 else 0
            nu2 = v2[i] if i<n2 else 0
            if nu1 <nu2:
                return -1
            elif nu1 > nu2:
                return 1
        return 0
