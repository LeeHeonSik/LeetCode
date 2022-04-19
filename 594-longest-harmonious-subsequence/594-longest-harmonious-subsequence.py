class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dic = collections.Counter(nums)
        ans = 0
        for i in dic:
            if i+1 in dic:
                ans = max(ans, dic[i] + dic[i+1])
        return ans