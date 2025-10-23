__author__ = 'meha001'

from typing import *

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        else:return n*2
            