class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)
        if target not in nums:
            return []
        
        k = nums.index(target)
        ans = [k]
        while True:
            k += 1
            try:
                if nums[k] != target:
                    return ans
                else:
                    ans.append(k)
            except:
                return ans