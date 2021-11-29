class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        ans = []
        for i in nums:
            if i % 2 == 1:
                odd.append(i)
            else:
                even.append(i)
        
        
        for i in range(len(nums)):
            if i % 2 == 1:
                ans.append(odd[i//2])
            else:
                ans.append(even[i//2])
        return ans