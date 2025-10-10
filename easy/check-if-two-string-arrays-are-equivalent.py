__author__ = 'meha001'

from typing import *

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1 = ''
        for i in word1:
            s1 += i
        s2 = ''
        for j in word2:
            s2 += j
        return s1 == s2