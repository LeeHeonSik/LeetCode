class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        r = []
        ans = []
        for i in range(len(matrix)):
            s = matrix[i].index(min(matrix[i]))
            r.append(s)
        
        for i in range(len(r)):
            c = []
            for j in matrix:
                c.append(j[r[i]])
            
            if c.index(max(c)) == i:
                ans.append(max(c))
        
        return ans