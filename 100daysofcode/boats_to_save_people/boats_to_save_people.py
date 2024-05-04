class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        le,ri = 0,len(people)-1
        b = 0
        while le <= ri:
            if people[le] + people[ri] <= limit:
                le += 1
            ri -= 1
            b += 1
        return b
        
