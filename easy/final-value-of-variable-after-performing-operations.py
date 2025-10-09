__author__ = 'meha001'

from typing import *

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        kol = 0
        for i in operations:
            if '-' in i:
                kol -= 1
            else:
                kol += 1

        return kol