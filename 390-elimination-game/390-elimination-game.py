class Solution:
    def lastRemaining(self, n: int) -> int:
        def dp(n):
            if n == 1:
                return 1
            if (n%2)==1:
                n -=1
            return n + 2*(1-dp(n//2))
        
        return dp(n)