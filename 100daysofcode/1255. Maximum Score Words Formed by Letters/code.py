class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        from collections import Counter
        s = {chr(i+97): score[i] for i in range(26)}
        def get_sc(word):
            return sum(s[le] for le in word)
        def dfs(ind, counter):
            if ind == len(words):
                return 0
            n = dfs(ind+1, counter)
            w = Counter(words[ind])
            if all(w[let] <= counter[let] for let in w):
                for l in w:
                    counter[l] -= w[l]
                t = get_sc(words[ind]) + dfs(ind+1, counter)
                for l in w:
                    counter[l] += w[l]
            else:
                t = 0
            return max(t,n)
        c = Counter(letters)
        return dfs(0, c)
