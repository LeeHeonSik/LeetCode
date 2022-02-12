class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        k = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                ans = max(ans, k)
                k = 0
            else:
                k += 1
        return max(ans, k)