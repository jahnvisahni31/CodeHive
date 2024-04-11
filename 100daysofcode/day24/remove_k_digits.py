class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        for di in num:
            while k > 0 and st and st[-1] > di:
                st.pop()
                k -= 1
            st.append(di)
        while k > 0:
            st.pop()
            k -= 1

        re = "".join(st).lstrip('0')
        return re if re else "0"

        
