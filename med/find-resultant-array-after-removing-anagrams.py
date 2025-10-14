__author__ = 'meha001'

from typing import *

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        t = [words[0]]
        for i in range(1, len(words)):
            if sorted(list(words[i])) != sorted(list(words[i-1])):
                t.append(words[i])
        return t