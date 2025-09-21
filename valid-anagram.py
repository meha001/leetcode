__author__ = 'meha001'

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return  sorted(s) == sorted(t)
    
    
print(Solution().isAnagram(s = "крыса", t = "автомобиль"))