__author__ = 'meha001'

from typing import *

class Solution:
    def countDigits(self, num: int) -> int:
        kol = sum([num % int(i) == 0 for i in str(num)])
        return kol