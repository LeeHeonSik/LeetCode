class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        benefit = 0
        low = 10**5
        for i in prices:
            if i > low:
                if benefit < i - low :
                    benefit = i - low
            elif i <= low :
                low = i
        return benefit