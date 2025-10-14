__author__ = 'meha001'

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        s = ''
        for i in word:
            s += i
            if i == ch: s = s[::-1]
        return s