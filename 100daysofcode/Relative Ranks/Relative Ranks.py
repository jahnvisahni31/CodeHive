class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        p = score[:]
        p.sort(reverse=True)
        t = {}
        for i, ke in enumerate(p):
            t[ke] = str(i+1)
        r = []
        for x in score:
            v = t[x]
            if v == "1":
                v = "Gold Medal"
            elif v == '2':
                v = "Silver Medal"
            elif v == "3":
                v = "Bronze Medal"
            r.append(v)
        return r
