class Solution:
    def isToeplitzMatrix(self, matrix):
        b = []
        for r, row in enumerate(matrix):
            if 0 < r < len(matrix):
                if b != row[1:]:
                    return False
            b = row[:-1]
        return True    