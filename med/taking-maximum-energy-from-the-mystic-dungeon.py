__author__ = 'meha001'

from typing import *

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        dp = energy[:]
        for i in range(len(energy) - k - 1, -1, -1):
            dp[i] += dp[i + k]
        return max(dp)