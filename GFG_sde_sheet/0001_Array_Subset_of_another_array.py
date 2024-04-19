from collections import Counter

def isSubset( a1, a2, n, m):
    c = Counter(a1)
    for num in a2:
        if c[num] < a2.count(num):
            return "No"
    return "Yes"

