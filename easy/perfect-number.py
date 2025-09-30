from math import *
__author__ = 'meha001'

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        
        summ = 0
        for i in range(1, int(sqrt(num))+1):
            if num % i == 0:
                summ += i
                if (i * i != 0):
                    summ += num / i
                
        return summ - num == num
    

print(Solution().checkPerfectNumber(100000))