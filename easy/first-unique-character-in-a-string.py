__author__ = 'meha001'
class Solution:
    def firstUniqChar(self, s: str) -> int:
        t = list('abcdefghijklmnopqrstuvwxyz')
        for i in range(len(s)):
            if s[i] in t:
                if s.count(s[i]) != 1:
                    t.remove(s[i])
                if s.count(s[i]) == 1:
                    return i
            
        return -1
    
print(Solution().firstUniqChar('loveleetcode'))