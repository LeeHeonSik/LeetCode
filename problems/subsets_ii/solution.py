class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i==0 or nums[i] != nums[i-1]:
                k=len(ans)
            for j in range(len(ans)-k,len(ans)):
                ans.append(ans[j]+[nums[i]])
        return ans