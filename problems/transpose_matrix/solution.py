class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans=[]
        for i in range(len(matrix[0])):
            t=[]
            for j in range(len(matrix)):
                t.append(matrix[j][i])
            ans.append(t)
        return ans
                          