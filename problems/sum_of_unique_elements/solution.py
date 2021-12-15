from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dic = Counter(nums)
        ans = 0
        for i, j in dic.items():
            if j == 1:
                ans += i
        return ans