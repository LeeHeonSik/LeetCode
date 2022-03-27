class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        k = sorted(nums)
        ans = []
        for i in range(len(nums)):
            ans.append(k.index(nums[i]))
        return ans