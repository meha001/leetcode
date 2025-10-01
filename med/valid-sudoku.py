__author__ = 'meha001'
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        print(board)
        for i in board:
            s = []
            for j in i:
                if j != '.' and j not in s:
                        s.append(j)
                elif j in s:
                    return False
        
        t = list(zip(*board))
        for i in t:
            s = []
            for j in i:
                if j != '.' and j not in s:
                        s.append(j)
                elif j in s:
                    return False
                
        for i in range(9):
            
            for j in range(9):
                t = []
                    
                if i == 0 and j == 0:
                    
                    if board[i][j] != '.':
                        t.append(board[i][j])
                    if board[i+1][j] != '.':
                        t.append(board[i+1][j])
                    if board[i+2][j] != '.':
                        t.append(board[i+2][j])
                    if board[i+1][j+1] != '.':
                        t.append(board[i+1][j+1])
                    if board[i+2][j+2] != '.':
                        t.append(board[i+2][j+2])
                        
                    if board[i+2][j+1] != '.':
                        t.append(board[i+2][j+1])
                    if board[i][j+1] != '.':
                        t.append(board[i][j+1])
                    if board[i][j+2] != '.':
                        t.append(board[i][j+2])
                    if board[i+1][j+2] != '.':
                        t.append(board[i+1][j+2])
                    print(1, t)
                if i == 0 and j == 3:
                    if board[i][j] != '.':
                        t.append(board[i][j])
                    if board[i+1][j] != '.':
                        t.append(board[i+1][j])
                    if board[i+2][j] != '.':
                        t.append(board[i+2][j])
                    if board[i+1][j+1] != '.':
                        t.append(board[i+1][j+1])
                    if board[i+2][j+2] != '.':
                        t.append(board[i+2][j+2])
                        
                    if board[i+2][j+1] != '.':
                        t.append(board[i+2][j+1])
                    if board[i][j+1] != '.':
                        t.append(board[i][j+1])
                    if board[i][j+2] != '.':
                        t.append(board[i][j+2])
                    if board[i+1][j+2] != '.':
                        t.append(board[i+1][j+2])
                    print(2, t)
                if i == 0 and j == 6:
                    if board[i][j] != '.':
                        t.append(board[i][j])
                    if board[i+1][j] != '.':
                        t.append(board[i+1][j])
                    if board[i+2][j] != '.':
                        t.append(board[i+2][j])
                    if board[i+1][j+1] != '.':
                        t.append(board[i+1][j+1])
                    if board[i+2][j+2] != '.':
                        t.append(board[i+2][j+2])
                        
                    if board[i+2][j+1] != '.':
                        t.append(board[i+2][j+1])
                    if board[i][j+1] != '.':
                        t.append(board[i][j+1])
                    if board[i][j+2] != '.':
                        t.append(board[i][j+2])
                    if board[i+1][j+2] != '.':
                        t.append(board[i+1][j+2])
                    print(3, t)
                if i == 3 and j == 0:
                    if board[i][j] != '.':
                        t.append(board[i][j])
                    if board[i+1][j] != '.':
                        t.append(board[i+1][j])
                    if board[i+2][j] != '.':
                        t.append(board[i+2][j])
                    if board[i+1][j+1] != '.':
                        t.append(board[i+1][j+1])
                    if board[i+2][j+2] != '.':
                        t.append(board[i+2][j+2])
                        
                    if board[i+2][j+1] != '.':
                        t.append(board[i+2][j+1])
                    if board[i][j+1] != '.':
                        t.append(board[i][j+1])
                    if board[i][j+2] != '.':
                        t.append(board[i][j+2])
                    if board[i+1][j+2] != '.':
                        t.append(board[i+1][j+2])
                    print(4, t)
                if i == 3 and j == 3:
                    if board[i][j] != '.':
                        t.append(board[i][j])
                    if board[i+1][j] != '.':
                        t.append(board[i+1][j])
                    if board[i+2][j] != '.':
                        t.append(board[i+2][j])
                    if board[i+1][j+1] != '.':
                        t.append(board[i+1][j+1])
                    if board[i+2][j+2] != '.':
                        t.append(board[i+2][j+2])
                        
                    if board[i+2][j+1] != '.':
                        t.append(board[i+2][j+1])
                    if board[i][j+1] != '.':
                        t.append(board[i][j+1])
                    if board[i][j+2] != '.':
                        t.append(board[i][j+2])
                    if board[i+1][j+2] != '.':
                        t.append(board[i+1][j+2])
                    print(5, t)    
                if i == 3 and j == 6:
                    if board[i][j] != '.':
                        t.append(board[i][j])
                    if board[i+1][j] != '.':
                        t.append(board[i+1][j])
                    if board[i+2][j] != '.':
                        t.append(board[i+2][j])
                    if board[i+1][j+1] != '.':
                        t.append(board[i+1][j+1])
                    if board[i+2][j+2] != '.':
                        t.append(board[i+2][j+2])
                        
                    if board[i+2][j+1] != '.':
                        t.append(board[i+2][j+1])
                    if board[i][j+1] != '.':
                        t.append(board[i][j+1])
                    if board[i][j+2] != '.':
                        t.append(board[i][j+2])
                    if board[i+1][j+2] != '.':
                        t.append(board[i+1][j+2])
                    print(6, t)
                if i == 6 and j == 0:
                    if board[i][j] != '.':
                        t.append(board[i][j])
                    if board[i+1][j] != '.':
                        t.append(board[i+1][j])
                    if board[i+2][j] != '.':
                        t.append(board[i+2][j])
                    if board[i+1][j+1] != '.':
                        t.append(board[i+1][j+1])
                    if board[i+2][j+2] != '.':
                        t.append(board[i+2][j+2])
                        
                    if board[i+2][j+1] != '.':
                        t.append(board[i+2][j+1])
                    if board[i][j+1] != '.':
                        t.append(board[i][j+1])
                    if board[i][j+2] != '.':
                        t.append(board[i][j+2])
                    if board[i+1][j+2] != '.':
                        t.append(board[i+1][j+2])
                    print(7, t)
                if i == 6 and j == 3:
                    if board[i][j] != '.':
                        t.append(board[i][j])
                    if board[i+1][j] != '.':
                        t.append(board[i+1][j])
                    if board[i+2][j] != '.':
                        t.append(board[i+2][j])
                    if board[i+1][j+1] != '.':
                        t.append(board[i+1][j+1])
                    if board[i+2][j+2] != '.':
                        t.append(board[i+2][j+2])
                        
                    if board[i+2][j+1] != '.':
                        t.append(board[i+2][j+1])
                    if board[i][j+1] != '.':
                        t.append(board[i][j+1])
                    if board[i][j+2] != '.':
                        t.append(board[i][j+2])
                    if board[i+1][j+2] != '.':
                        t.append(board[i+1][j+2])
                    print(8, t)
                if i == 6 and j == 6:
                    if board[i][j] != '.':
                        t.append(board[i][j])
                    if board[i+1][j] != '.':
                        t.append(board[i+1][j])
                    if board[i+2][j] != '.':
                        t.append(board[i+2][j])
                    if board[i+1][j+1] != '.':
                        t.append(board[i+1][j+1])
                    if board[i+2][j+2] != '.':
                        t.append(board[i+2][j+2])
                        
                    if board[i+2][j+1] != '.':
                        t.append(board[i+2][j+1])
                    if board[i][j+1] != '.':
                        t.append(board[i][j+1])
                    if board[i][j+2] != '.':
                        t.append(board[i][j+2])
                    if board[i+1][j+2] != '.':
                        t.append(board[i+1][j+2])
                        
                    print(9, t)
                    
                if len(t) != len(set(t)):
                    print(t)
                    return False
        return True
        
print(Solution().isValidSudoku(
   [["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]
   ))