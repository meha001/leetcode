__author__ = 'meha001'

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        phoneMap = {
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl",
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz"
        }
        if len(digits) == 0:
            return []
        result = [""]
    
        for digit in digits:
            new_result = []
            for combination in result:
                for letter in phoneMap[digit]:
                    new_result.append(combination + letter)
            result = new_result
        
        return result
    
print(Solution().letterCombinations("2345"))
