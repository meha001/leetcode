__author__ = 'meha001'

from typing import *
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix) - 1):
            t = []
            for j in range(len(matrix[i]) - 1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True
        return len(set(t)) == 1
    