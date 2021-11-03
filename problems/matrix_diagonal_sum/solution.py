class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        L = len(mat)
        ans = 0
        if L % 2 == 1 :
            for i in range(L):
                ans += mat[i][i]
                ans += mat[L-i-1][i]
            return ans - mat[L//2][L//2]
        elif L % 2 == 0 :
            for i in range(L):
                ans += mat[i][i]
                ans += mat[L-i-1][i]
            return ans