class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1 :
            return 0
        nums.sort(reverse=True)
        ans = 10**6
        for i in range(len(nums)-k+1):
            if ans > nums[i] - nums[i + k -1]:
                ans = nums[i] - nums[i + k -1]
        return ans