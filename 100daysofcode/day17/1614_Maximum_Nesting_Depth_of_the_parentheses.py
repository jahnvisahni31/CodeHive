class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        max_depth = 0
        current_depth = 0

        for char in s:
            if char == '(':
                stack.append(char)
                current_depth = len(stack)
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                if stack:
                    stack.pop()
                    current_depth = len(stack)
                else:
                    return -1  # Invalid VPS

        if stack:
            return -1  # Invalid VPS
        else:
            return max_depth
