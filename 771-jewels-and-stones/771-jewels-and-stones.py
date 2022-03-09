class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        stones = collections.Counter(stones)
        jewels = collections.Counter(jewels)
        for i in jewels.keys():
            if i in stones.keys():
                ans += stones[i]
        return ans