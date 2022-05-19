import numpy as np
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N = len(nums)
        nums = set(nums)
        result = []
        for i in range(1, N+1):
            if i not in nums:
                result.append(i)
        return result