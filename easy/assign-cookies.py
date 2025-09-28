__author__ = 'meha001'

class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        kol = 0
        for j in range(len(g)):
            i = 0
            while len(s) != 0 and i < len(s):
                if g[j] <= s[i]:
                    s.remove(s[i])
                    kol += 1
                    break
                else:
                    i += 1            
            else:
                break
        
        return (kol)
(Solution().findContentChildren(g = [1,2], s = [1,2,3]))