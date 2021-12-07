from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        k = len(nums)//2
        
        dic = Counter(nums)
        
        for i in dic.keys():
            if dic[i] == k:
                return i