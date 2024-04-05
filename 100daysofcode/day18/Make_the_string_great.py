class Solution:
    def makeGood(self, s: str) -> str:
        st = []
        for cha in s:
            if st and abs(ord(st[-1]) - ord(cha)) == 32:
                st.pop()
            else:
                st.append(cha)
        return ''.join(st) 
