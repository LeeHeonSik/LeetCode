class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        ans = [0, 1]
        if n == 0:
            return 0
        
        for i in range(2, n+1):
            if i % 2 == 0 :
                ans.append(ans[i//2])
            else:
                ans.append(ans[i//2] + ans[(i+1)//2])
        return max(ans)
                