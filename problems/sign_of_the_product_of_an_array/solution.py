class Solution:
    def arraySign(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] >= 0:
                if nums[i] == 0:
                    return 0
                else:
                    n = i
                    break
        if n % 2 == 1:
            return -1
        else:
            return 1