class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(len(nums)):
            if abs(nums[i]) < abs(ans):
                ans = nums[i]
            elif abs(nums[i]) == abs(ans):
                if nums[i] > ans:
                    ans = nums[i]
        return ans