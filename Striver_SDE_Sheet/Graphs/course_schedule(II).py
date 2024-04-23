class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        gra = {c: [] for c in range(numCourses)}
        for cf,pre in prerequisites:
            gra[cf].append(pre)
        cor = []
        visit, cycle = set(), set()
        def dfs(co):
            if co in cycle:
                return False
            if co in visit:
                return True
            cycle.add(co)
            for pre in gra[co]:
                if not dfs(pre):
                    return False
            cycle.remove(co)
            visit.add(co)
            cor.append(co)
            return True
        for cour in range(numCourses):
            if not dfs(cour):
                return []
        return cor
