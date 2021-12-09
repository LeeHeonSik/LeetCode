class Solution:
    def minOperations(self, s: str) -> int:
        ans1, ans2 = 0, 0
        x,y = '0','1'
        for i in s:
            if i != x:
                ans1 += 1
            if i != y:
                ans2 += 1
            
            x,y = y,x
            
            
        return min(ans1,ans2)