class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd = [nums[i] for i in range(1,len(nums),2)]
        even = [nums[i] for i in range(0,len(nums),2)]

        odd = sorted(odd, reverse = True)
        even = sorted(even)

        
        ans = []
        for i in range(len(nums)//2):
            ans.append(even[i])
            ans.append(odd[i])
            
        if len(ans) == len(nums):
            return ans
        else:
            return ans + [even[-1]]