__author__ = 'meha001'

from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
        result = [[0] * cols for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                total = 0
                count = 0
                
                for di in (-1, 0, 1):
                    for dj in (-1, 0, 1):
                        ni, nj = i + di, j + dj
                        if 0 <= ni < rows and 0 <= nj < cols:
                            total += img[ni][nj]
                            count += 1
                
                result[i][j] = total // count
        
        return result