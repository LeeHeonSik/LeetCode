class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            c = nums[i+1::].count(nums[i])
            ans +=c
        return ans