__author__ = 'meha001'

from typing import *

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        t = []
        for i in range(len(boxes)):
            s = 0
            for j in range(len(boxes)):
                if i != j:
                    if boxes[j] == '1':
                        s += abs(i-j)
            t.append(s)
        return t