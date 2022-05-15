class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        ans = nums[:k]
        for i in range(k,len(nums)):
            t = min(ans)
            if t < nums[i]:
                ans.remove(t)
                ans.append(nums[i])
        return ans