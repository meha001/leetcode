__author__ = 'meha001'

from typing import *

def func(n):
    n = str(n)
    for i in str(n):
        if n.count(i) != int(i):
            return False
    return True   

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        n = n + 1
        while True:
            if func(n):
                return n
            n += 1