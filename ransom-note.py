__author__ = 'meha001'

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = sorted(ransomNote)
        magazine = sorted(magazine)
        flag = 1
        for i in ransomNote:
            if ransomNote.count(i) > magazine.count(i):
                 flag = 0
        return bool(flag)
print(Solution().canConstruct('a', 'b'))