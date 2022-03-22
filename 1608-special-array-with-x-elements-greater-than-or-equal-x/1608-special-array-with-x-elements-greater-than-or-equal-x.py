class Solution:
    def specialArray(self, nums: List[int]) -> int:
        ans = 0
        n = max(nums)
        for i in range(n+1):
            k = 0
            for j in range(len(nums)):
                if nums[j] >= i:
                    k += 1
            if k == i:
                return k
        return -1