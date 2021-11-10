class Solution:
    def fib(self, n: int) -> int:
        ans = [0, 1]
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        for i in range(2, n+1):
            c = ans[i-1] + ans[i-2]
            ans.append(c)
        return ans[-1]