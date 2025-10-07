__author__ = 'meha001'

from typing import *

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:

        t = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        print(len(t))
        
        twords = []
        for i in (words):
            s = ''
            for j in range(len(i)):
                s += t[ord(i[j]) - 96 ]
            
            twords.append(s)
            
        print(len(set(twords)))
    
Solution().uniqueMorseRepresentations(['a', 'jin', 'zen'])