class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        for i in range(1,len(nums)):
            b = nums[i-1]
            a = nums[i]
            if b >= a:
                nums[i] = b + 1
                ans += b - a + 1
        return ans
            