class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = len(nums) // 2
        dic={}
        for i in nums:
            dic[i] = dic.get(i,0)+1
        for j in dic:
            if dic[j] > a:
                return j