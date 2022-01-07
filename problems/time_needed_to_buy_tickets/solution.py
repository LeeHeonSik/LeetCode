class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        while True:
            for j in range(len(tickets)):
                if tickets[j] != 0:
                    tickets[j] -= 1
                    ans += 1
                if tickets[k] == 0:
                    return ans