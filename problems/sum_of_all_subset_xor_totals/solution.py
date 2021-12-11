from itertools import combinations
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = sum(nums)
        for i in range(2, len(nums)+1):
                for j in combinations(nums, i):
                    c = 0
                    for k in j:
                        c = c ^ k
                    ans += c
        return ans