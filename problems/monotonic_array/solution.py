class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = sorted(nums)
        if n == nums or n[::-1] == nums:
            return True
        return False