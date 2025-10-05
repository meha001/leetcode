__author__ = 'meha001'

from typing import List


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        kol = 0
        t = set()
        for i in (words):
            if i[::-1] in t:
                kol += 1
            t.add(i)
            
        return kol
