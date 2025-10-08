__author__ = 'meha001'

from typing import *

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:

        t = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        
        twords = []
        for i in (words):
            s = ''
            for j in range(len(i)):
                # print(ord(i[j]) - 96)
                s += t[ord(i[j]) - 97 ]
            
            twords.append(s)
            
        return len(set(twords))
    
Solution().uniqueMorseRepresentations(['a', 'jin', 'zen'])