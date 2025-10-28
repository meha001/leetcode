__author__ = 'meha001'
from typing import *
from collections import *
from itertools import *

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        t = []
        for i in bank:
            if i.count('1') != 0:
                t.append(i.count('1'))
                
        kol = 0
        for i in range(len(t)-1):
            kol += t[i] * t[i+1]
        return kol        