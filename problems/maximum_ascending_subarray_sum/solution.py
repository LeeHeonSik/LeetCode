class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = nums[0]
        c = 0
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                ans += nums[i]
            else:
                if c < ans :
                    c = ans
                ans = nums[i]
        return max(c,ans)