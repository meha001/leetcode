__author__ = 'meha001'

from typing import List

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x = ord(coordinates[0]) - 96
        y = int(coordinates[1])
        return bool((x + y) % 2)
        