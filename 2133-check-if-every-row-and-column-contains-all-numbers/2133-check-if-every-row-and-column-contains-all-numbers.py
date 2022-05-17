import numpy as np
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        matrix = np.array(matrix)
        n = len(matrix)
        arr = [i+1 for i in range(n)]
        for i in range(n):
            if sorted(matrix[i]) != arr:
                return False
            if sorted(matrix[:,i]) != arr:
                return False
        return True