import numpy as np
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        num_s = set(nums)
        for i in range(1, len(nums)+1):
            if i not in num_s:
                ans.append(i)
        return ans