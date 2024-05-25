class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        def dfs(i,v):
            if i == len(s):
                res.append(v[1:])
                return
            for w in wordDict:
                if s[i:].startswith(w):
                    dfs(i + len(w),v + " " + w)
        dfs(0,'')
        return res
