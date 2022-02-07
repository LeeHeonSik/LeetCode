class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        _max = 2147483647
        st = nums[0]
        for i in range(1, len(nums)):
            if nums[i]> _max:
                return True
            elif nums[i] > st:
                _max = nums[i]
            else:
                st = nums[i]
        return False