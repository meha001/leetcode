__author__ = 'meha001'
from typing import *

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        st = ''
        for i in words:
            st += i
            if s == st:
                return True
        return False