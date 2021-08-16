from collections import Counter
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        
        if max(len(nums1),len(nums2)) > min(len(nums1),len(nums2)) * 6 :
            return -1
        
        if sum(nums2) > sum(nums1):
            n1 = nums2
            n2 = nums1
        else :
            n1 = nums1
            n2 = nums2
            
        diff = sum(n1) - sum(n2)
        dic1 = Counter(n1)
        dic2 = Counter(n2)
        ans=0
        
        for i in range(1,7):
            j = 7 - i
            t = (dic1[j] + dic2[i]) * (j-1)
            
            if t >= diff :
                return ans + ((diff-1)//(j-1)+1)
            else:
                diff -= t
                ans += dic1[j] + dic2[i]