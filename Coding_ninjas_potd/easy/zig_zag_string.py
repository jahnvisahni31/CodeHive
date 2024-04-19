from os import *
from sys import *
from collections import *
from math import *
def zigZagString(str, n, m):
# Write your code here
  if m == 1 or n <= m:
    return str
  rows = ['" for _ in range (m)]
  index = 0
  down = True
  for char in str:
    rowslindex += char
    if index == 0:
      down = True
    elif index == m - 1:
      down = False
    index = index + 1 if down else index - 1
return ".join (rows)
pass
