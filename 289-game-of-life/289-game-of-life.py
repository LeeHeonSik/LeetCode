class Solution:
    def check(self, row, col, x : int, y : int, prev : list[list[int]], board : list[list[int]]):
        c = 0
            
        
        
        for i in range(3):
            for j in range(3):
                if (0 <= x-1+j < row) and (0 <= y-1+i < col) and (prev[x-1+j][y-1+i]) == 1:
                    c += 1
        n = board[x][y]
        return self.conditions(c, n)      
            
    def conditions(self, c, n):
        if (n == 1):
            c -= 1
            if (c <2) or c > 3:
                return 0
            else:
                return 1
        else:
            if c == 3: return 1
            else : return 0
                
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        prev = copy.deepcopy(board)
        row = len(board)
        col = len(board[0])
        
        for a in range(row):
            for b in range(col):
                board[a][b] = self.check(row, col, a, b, prev, board)
        