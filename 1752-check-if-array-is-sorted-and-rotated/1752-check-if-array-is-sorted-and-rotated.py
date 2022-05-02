class Solution:
    def check(self, nums: List[int]) -> bool:
        c = 0
        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:
                c = i
        nums = nums[c::] + nums[:c]
        k = sorted(nums)
        return k == nums