class Solution:
    def firstUniqChar(self, s: str) -> int:
        t = set(s)
        for i in t:
            if s.count(i) == 1:
                return s.index(i)
            
        return -1
    
print(Solution().firstUniqChar('leetcode'))