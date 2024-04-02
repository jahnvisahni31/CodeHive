class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}
        for i in range(len(s)):
            if s[i] in s_map:
                if s_map[s[i]] != t[i]:
                    return False
            else:
                s_map[s[i]] = t[i]
            if t[i] in t_map:
                if t_map[t[i]] != s[i]:
                    return False
            else:
                t_map[t[i]] = s[i]
        return True
