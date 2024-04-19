from os import *
from sys import *
from collections import *
from math import *
from typing import List

def largestSubMatrix(n: int, m: int, arr: List[List[int]]) -> int:
    # write your code here
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                arr[0][j] = -1

    maxArea = 0
    rows, cols = len(arr), len(arr[0])
    prefixSum = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            top = prefixSum[i - 1][j] if i > 0 else 0
            left = prefixSum[i][j - 1] if j > 0 else 0
            topLeft = prefixSum[i - 1][j - 1] if i > 0 and j > 0 else 0
            prefixSum[i][j] = arr[i][j] + top + left - topLeft

    for r1 in range(rows):
        for r2 in range(r1, rows):
            countMap = {0: -1}
            for c in range(cols):
                cur = prefixSum[r2][c] - (prefixSum[r1 - 1][c] if r1 > 0 else 0)
                if cur in countMap:
                    area = (r2 - r1 + 1) * (c - countMap[cur])
                    maxArea = max(maxArea, area)
                else:
                    countMap[cur] = c

    return maxArea

# pass
