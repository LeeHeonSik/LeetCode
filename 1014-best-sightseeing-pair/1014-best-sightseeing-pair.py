class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        x = values[0]
        y = 0
        for i in range(1, len(values)):
            y = max(y, x + values[i] - i)
            x = max(x, values[i] + i)
        return y