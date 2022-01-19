class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        _set = set()

        for i in range(len(nums)):
            if not(i > 2 and nums[i] == nums[i-2]): 
                for j in range(i+1, len(nums)):
                    s = -(nums[i]+nums[j])
                    if s in _set:
                        ans.add((nums[i], nums[j], s))
            _set.add(nums[i])
        return list(ans)