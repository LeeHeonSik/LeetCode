class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic={}
        l=50000
        for i in nums:
            dic[i]=dic.get(i,0)+1
        m=max(dic.values())
        for j in dic:
            if dic[j] == m :
                s=nums.index(j)
                e=len(nums) - nums[::-1].index(j)
                if l > e-s:
                    l=e-s
        return l