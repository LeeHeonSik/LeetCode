class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n-1):
            if nums[i+1] <= nums[i]:
                ans += nums[i] - nums[i+1] + 1
                nums[i+1] = nums[i] + 1
                
        return ans