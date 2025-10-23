__author__ = 'meha001'

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        def func(s):
            return len(set(list(s))) == 1
        st = s
        while len(st)!=2:
            st = ''
            for i in range(len(s)-1):
                st += (int(s[i]) + int(s[i+1])) % 10
            s = st
            
        return func(s)