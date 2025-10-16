__author__ = 'meha001'
from typing import *

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(i) for i in accounts])