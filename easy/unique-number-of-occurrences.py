__author__ = 'meha001'
from typing import *

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = []
        t = set(arr)
        n = len(arr)
        for i in t:
            freq.append(arr.count(i))
            
        return len(set(freq)) == len(freq)
        