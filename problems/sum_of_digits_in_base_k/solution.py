class Solution:
    def sumBase(self, n: int, k: int) -> int:
        ans = 0
        if n < k :
            return n
        for i in range(6,-1,-1):
            c = n//k**i
            n -= c *(k**i)
            ans+=c
        return ans