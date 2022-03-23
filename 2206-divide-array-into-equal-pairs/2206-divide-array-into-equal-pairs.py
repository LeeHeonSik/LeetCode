class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dic = collections.Counter(nums)
        if all((i%2 == 0) for i in dic.values()):
            return True
        return False