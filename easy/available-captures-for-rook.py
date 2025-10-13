__author__ = 'meha001'
from typing import *

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        x = -1
        y = -1
        kol = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    x = j
                    y = i
        # print(x, y)
        
        for i in range(x, 8):
            if board[y][i] == 'B':
                break
            if board[y][i] == 'p':
                kol += 1
                
                break
            
        for i in range(x, -1, -1):
            if board[y][i] == 'B':
                break
            if board[y][i] == 'p':
                kol += 1
                break
            
        for i in range(y, 8):
            if board[i][x] == 'B':
                break
            if board[i][x] == 'p':
                kol += 1
                break
            
        for i in range(y, -1, -1):
            if board[i][x] == 'B':
                break
            if board[i][x] == 'p':
                kol += 1
                break
        return kol
                                    
print(Solution().numRookCaptures(
    [[".",".",".",".",".",".",".","."],
     [".",".",".","p",".",".",".","."],
     [".",".",".","R",".",".",".","p"],
     [".",".",".",".",".",".",".","."],
     [".",".",".",".",".",".",".","."],
     [".",".",".","p",".",".",".","."],
     [".",".",".",".",".",".",".","."],
     [".",".",".",".",".",".",".","."]]
))                
        
        
        



