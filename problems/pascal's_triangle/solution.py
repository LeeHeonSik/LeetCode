class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        b = []
        for i in range(numRows-1):
            for j in range(len(ans[i])-1):
                b.append(ans[i][j] + ans[i][j+1])
            a = [1] + b + [1]
            b.clear()
            ans.append(a)
        return ans