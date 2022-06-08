class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for i in range(len(accounts)):
            ans = max(sum(accounts[i]), ans)
        return ans