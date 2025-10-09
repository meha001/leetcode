__author__ = 'meha001'

from typing import *

class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        result = []
        temp = n
        
        for i in range(k - 1):
            for divisor in range(2, int(temp**0.5) + 1):
                if temp % divisor == 0:
                    result.append(divisor)
                    temp //= divisor
                    break
            else:
                num = int(temp ** (1/(k - i)))
                result.append(num)
                temp //= num
        
        result.append(temp)
        return sorted(result)

print(Solution().minDifference(100, 2))