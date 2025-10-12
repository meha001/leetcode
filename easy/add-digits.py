__author__ = 'meha001'


class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) != 1:
            num = sum(list(str(num)))
        return num