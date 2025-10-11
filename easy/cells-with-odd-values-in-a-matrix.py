__author__ = 'meha001'

from typing import List

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        for i in (indices):
            
                for k in range(n):
                     matrix[i[0]][k] += 1
                
                for k2 in range(m):
                     matrix[k2][i[1]] += 1
        
        
        kol = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] % 2 == 1:
                    kol += 1
                
        return kol 