__author__ = 'meha001' 

class Solution:
    def countBits(self, n: int) -> list[int]:
        return [bin(i).count('1') for i in range(0, n+1)]


print(Solution().countBits(5))
