class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        for i in range(len(nums)):
            k = nums[i]
            right -= k
            if left == right:
                return i
            left += k
        return -1