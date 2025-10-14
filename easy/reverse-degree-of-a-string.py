__author__ = 'meha001'

class Solution:
    def reverseDegree(self, s: str) -> int:
        summ = 0
        for i in range(len(s)):
            summ += (27 - (ord(s[i]) - 96)) * (i + 1)
        return summ