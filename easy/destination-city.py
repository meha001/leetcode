__author__ = 'meha001'

from typing import *

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s = set()
        for i in paths:
            s.add(i[0])
            s.add(i[1])
        k1 = -1
        k2 = -1
        for i in s:
            k1 = -1
            k2 = -1
            for j in paths:
                if i == j[0]:
                    k1 = 1
                if i == j[1]:
                    k2 = 1
                
            if k1 == -1 and k2 == 1:
                return i