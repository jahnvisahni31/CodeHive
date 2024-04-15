import bisect
class Solution:
    def countElements(self, a, b, n, query, q):
        # code here
        s = sorted(b)
        re = []
        for qu in query:
            x = qu
            pos = bisect.bisect_right(s, a[x])
            c = pos
            re.append(c)
        return re
