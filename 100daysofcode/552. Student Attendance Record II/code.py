from functools import cache

@cache
def countRecords(n, conseqLates, absences):
    if n==0:
        return 1

    count = 0

    # P
    count += countRecords(n-1, 0, absences)

    # A
    if absences < 1:
        count += countRecords(n-1, 0, absences+1)

    # L
    if conseqLates < 2:
        count += countRecords(n-1, conseqLates+1, absences)

    return count % (pow(10,9)+7)


class Solution:
    def checkRecord(self, n: int) -> int:
        return countRecords(n,0,0)
        
