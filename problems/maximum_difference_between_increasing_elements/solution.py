class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        rm = sorted(nums, reverse = True)
        if nums == rm:
            return -1
        m=0
        for i in range(len(nums)):
            n = max(nums[i::]) - nums[i]
            if n > m :
                m = n
        return m