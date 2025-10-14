__author__ = 'meha001'

class Solution:
    def minLength(self, s: str) -> int:
        tlist = [s[0]]
        for i in range(1, len(s)):
            if tlist and tlist[-1] + s[i] == 'AB':
                tlist.pop()
            elif tlist and tlist[-1] + s[i] == 'CD':
                tlist.pop()
            else:
                tlist.append(s[i])
        return len(tlist)