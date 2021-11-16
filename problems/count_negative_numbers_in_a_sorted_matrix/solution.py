class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c = 0
        row = len(grid)
        column = len(grid[0])
        for i in range(row):
            for j in range(column):
                if grid[i][j] < 0:
                    c += (row-i)
                    column -= 1
        return c