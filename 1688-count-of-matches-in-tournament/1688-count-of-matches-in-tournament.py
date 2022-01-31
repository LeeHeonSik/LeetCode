class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while n > 1:
            a = n % 2
            n //= 2
            ans += a
            ans += n
        return ans
            