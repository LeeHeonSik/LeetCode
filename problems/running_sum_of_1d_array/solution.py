class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[0]
        ans[0]=nums[0]
        for i in range(1,len(nums)):
            ans.append(ans[i-1] + nums[i])
        return ans