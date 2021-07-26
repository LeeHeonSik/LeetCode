class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ans=0
        nums.append(target)
        nums.sort()
        ans=nums.index(target)
        return ans