class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans = []
        for i in nums[0]:
            if all(i in j for j in nums):
                ans.append(i)
        ans = sorted(ans)
        return ans