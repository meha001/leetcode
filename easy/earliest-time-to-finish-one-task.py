__author__ = 'meha001'
from typing import *

class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        tmin = float('inf')
        for i in tasks:
            tmin = min(tmin, sum(i))
        print(tmin)
Solution().earliestTime([[1, 6], [2, 3]])