__author__ = 'meha001'
from collections import defaultdict
class Solutions:
    def longestPalindrome(s: str) -> int:
    
        freq = defaultdict(int)
        # print(freq)
        for char in s:
            freq[char] += 1
            
        length = 0
        has_odd = False
        
        for count in freq.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                has_odd = True
                
        if has_odd:
            length += 1
            
        return (length)
    
print(Solutions.longestPalindrome('abccccdd'))