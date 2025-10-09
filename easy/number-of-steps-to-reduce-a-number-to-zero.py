__author__ = 'meha001'


class Solution:
    def numberOfSteps(self, num: int) -> int:
        kol = 0
        while num != 0:
            if num % 2 == 0:
                num //= 2
                kol += 1
            else:
                num -= 1
                kol += 1
        return kol