class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        ans = 0
        cost = sorted(cost, reverse = True)
        n = len(cost)
        for i in range(0, n-2, 3):
            ans += cost[i]
            ans += cost[i+1]
        if n % 3 == 1:
            ans += cost[-1]
        elif n % 3 == 2:
            ans += cost[-1]
            ans += cost[-2]
        return ans