class Solution:
    def checkValidString(self, s: str) -> bool:
        l = 0
        h = 0
        for char in s:
            if char == '(':
                l += 1
                h += 1
            elif char == ')':
                l = max(l - 1, 0)
                h -= 1
                if h < 0:
                    return False
            else:
                l = max(l - 1, 0)
                h += 1
    
        return l == 0
        
