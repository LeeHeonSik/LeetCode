class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        c = 0
        l = []
        if 1 not in nums:
            return True
        m = nums.index(1)
        for i in nums[m+1::]:
            if i == 1:
                l.append(c)
                c = 0
            elif i == 0 :
                c +=1
        
        return all(i >= k for i in l)