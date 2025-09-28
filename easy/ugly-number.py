__author = 'meha001'

class Solution:
    def isUgly(self, n: int) -> bool:
        for i in range(32):
            for j in range(21):
                for k in range(14):
                    if ((2 ** i) * (3 ** j) * (5 ** k) == n):
                        return True
        return False
    
print(Solution().isUgly(14))