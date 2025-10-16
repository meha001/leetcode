__author__ = 'meha001'

from typing import *

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        bits = bits[-2::-1]
        if 0 in bits:
            bits = bits[:bits.index(0, 0)]
        return bits.count(1) % 2 == 0