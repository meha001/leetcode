__author__ = 'meha001'
from typing import *
from collections import *
from itertools import *

class Solution:
    def totalMoney(self, n: int) -> int:
        mondey = 1
        HercyMoney = 0
        k = mondey
        for i in range(1, n+1):
            HercyMoney += k
            k += 1
            print(HercyMoney)
            if i % 7 == 0:
                mondey += 1
                k = mondey
        return HercyMoney