__author__ = 'meha001'

class Solution:
    def isHappy(self, n: int) -> bool:
        t = [n]
        s = 0
        while n != 1 and t.count(n) == 1:
            s = 0
            for i in str(n):
                s += int(i)**2
            print(s)
            n = s
            t.append(s)
        return n == 1
    
print(Solution().isHappy(19))