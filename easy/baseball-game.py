__author__ = 'meha001'

from typing import *


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        tlist = []
        for i in operations:
            if i not in 'CD+':
                tlist.append(int(i))
            if i == 'C':
                tlist.pop()
            if i == '+':
                tlist.append(tlist[-1] + tlist[-2])
            if i == 'D':
                tlist.append(tlist[-1] * 2)
            print(tlist)
        return sum(tlist)