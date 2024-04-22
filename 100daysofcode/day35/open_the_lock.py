class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        qu = deque([('0000', 0)])
        vi = set(deadends)
        if '0000' in vi:
            return -1
        while qu:
            cu, tu = qu.popleft()
            if cu == target:
                return tu
            for i in range(4):
                for move in (+1, -1):
                    ne = (int(cu[i]) + move) % 10
                    neighbor = cu[:i] + str(ne) + cu[i + 1:]
                    if  neighbor not in vi:
                        vi.add((neighbor))
                        qu.append((neighbor, tu+1))
        return -1
