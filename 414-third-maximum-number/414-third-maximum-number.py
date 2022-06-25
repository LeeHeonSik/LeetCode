class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(sorted(list(set(nums)))) < 3:
            return max(nums)
        return sorted(list(set(nums)))[-3]