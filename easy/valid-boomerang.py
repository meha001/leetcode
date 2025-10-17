__author__ = 'meha001'
from typing import *
import math
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        
        if points[0] == points[1] or points[0] == points[2] or points[1] == points[2]:
            return False
        
        area = abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2
        return area != 0