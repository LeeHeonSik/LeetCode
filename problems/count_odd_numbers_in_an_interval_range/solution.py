class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return int((high-low+2)/2) if (high%2) else int((high-low+1)/2)