class Solution:
    def numWaterBottles(self, B: int, E: int) -> int:
        ans = B
        while B >= E:
            k = B // E
            ans += k
            B -= k * (E-1)
        return ans