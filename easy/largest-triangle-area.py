__author__ = 'meha001'
from typing import *

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        tmax = 0
        
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                for z in range(j + 1, len(points)):
                    x3, y3 = points[z]
                    tmax = max((1/2) * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)), tmax)
        return tmax