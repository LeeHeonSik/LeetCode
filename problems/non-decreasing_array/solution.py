class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = sorted(nums)
        if n == nums or len(nums)<=2:
            return True
        
        fst = (nums[0] <= nums[1])
        for i in range(1, len(nums)-1):
            if nums[i] > nums[i+1]:
                if fst:
                    if nums[i+1] < nums[i-1]:
                        nums[i+1] = nums[i]
                    fst = False
                else:
                    return fst
        return True