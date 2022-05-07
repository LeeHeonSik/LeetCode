class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = collections.Counter(nums)
        if len(dic.keys()) < len(nums):
            return True
        return False