class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        prev = 0
        flag = False
        nums.append(1001)
        i, n = 0, len(nums) - 1
        while i < n:
            if prev < nums[i] < nums[i+1]:
                prev = nums[i]
            else:
                if flag:
                    return False
                flag = True
                if nums[i+1] <= prev:
                    prev = nums[i]
                    i += 1
            i += 1
        
        return True