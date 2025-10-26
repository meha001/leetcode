__author__ = 'meha001'
from typing import *
from collections import *
from itertools import *


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        return [pref[0]] + [pref[i] ^ pref[i-1] for i in range(1, len(pref))]