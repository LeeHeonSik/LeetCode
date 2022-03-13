class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = math.floor(math.sqrt(2*n + 1/4) - 1/2)
        return k