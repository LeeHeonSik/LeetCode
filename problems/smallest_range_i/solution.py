class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        c = max(nums) - min(nums)
        if c >= 2*k:
            return c - 2*k
        else:
            return 0