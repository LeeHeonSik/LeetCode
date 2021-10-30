class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = []
        c = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                c += 1
            else:
                ans.append(c)
                c = 1
        ans.append(c)
        return max(ans)