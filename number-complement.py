__author__ = 'meha001'



class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num)[2:]
        s = ''
        for i in num:
            if i == '0': s += '1'
            else: s += '0'
        return int(s, 2)
    
print(Solution().findComplement(1))