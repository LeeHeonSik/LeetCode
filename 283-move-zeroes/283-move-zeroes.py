class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = []
        for i in range(len(nums)):
            if nums[i] == 0:
                k.append(i)
        
        for j in k[::-1]:
            nums.pop(j)
            nums.append(0)
            