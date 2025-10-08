__author__ = 'meha001'
from typing import *


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        s = ''
        paragraph = paragraph.lower()
        # banned = banned.lower()
        twords = []
        
        for i in (paragraph):
            if i.isalpha():
                s += i
            else:
                if s != '':
                    twords.append(s)
                s = ''
        if s != '':
            twords.append(s)
        
        s = ''; tmax = 0
        for i in (twords):
            if twords.count(i) > tmax and i not in banned:
                s = i
                tmax = twords.count(i)
        return(s)
        
            
        
Solution().mostCommonWord('Bob hit a ball, the hit BALL flew far after it was hit.', 'hit')