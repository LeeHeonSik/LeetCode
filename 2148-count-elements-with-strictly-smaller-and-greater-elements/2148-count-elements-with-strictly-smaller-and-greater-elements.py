class Solution:
    def countElements(self, nums: List[int]) -> int:
        ans = 0
        m, M = min(nums), max(nums)
        for i in range(len(nums)):
            if m < nums[i] < M:
                ans += 1
        return ans