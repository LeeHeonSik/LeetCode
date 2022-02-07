class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        _max = 2147483647
        st = nums[0]
        for i in nums[1::]:
            if i > _max:
                return True
            elif i > st:
                _max = i
            else:
                st = i
        return False